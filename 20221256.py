import tkinter as tk
from tkinter import messagebox
import random

# フランス語とその日本語の意味を辞書として定義
quiz_data = {
    "Bonjour": "こんにちは",
    "Merci": "ありがとう",
    "Chat": "猫",
    "Chien": "犬",
    "Pomme": "りんご",
    "Livre": "本",
    "Voiture": "車",
    "Maison": "家",
    "Amour": "愛",
    "Soleil": "太陽"
}

# クラスの定義
class FrenchQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("フランス語クイズ")
        self.score = 0
        self.questions_asked = []
        self.total_questions = len(quiz_data)
        self.current_word = ""
        self.correct_answer = ""

        # ウィジェットのレイアウト
        self.label_title = tk.Label(root, text="フランス語クイズ", font=("Helvetica", 16, "bold"))
        self.label_title.pack(pady=10)

        self.label_word = tk.Label(root, text="", font=("Helvetica", 14))
        self.label_word.pack(pady=10)

        self.entry_answer = tk.Entry(root, font=("Helvetica", 14))
        self.entry_answer.pack(pady=10)

        self.button_submit = tk.Button(root, text="答える", command=self.check_answer)
        self.button_submit.pack(pady=5)

        self.label_feedback = tk.Label(root, text="", font=("Helvetica", 12))
        self.label_feedback.pack(pady=5)

        self.label_score = tk.Label(root, text=f"現在のスコア: {self.score}/{self.total_questions}", font=("Helvetica", 12))
        self.label_score.pack(pady=10)

        self.button_restart = tk.Button(root, text="再挑戦", command=self.restart_quiz)
        self.button_restart.pack(pady=5)

        # 初始クイズの出題
        self.next_question()

    def next_question(self):
        # 残りの問題があるか確認
        if len(self.questions_asked) >= self.total_questions:
            messagebox.showinfo("クイズ終了", f"あなたの最終スコアは {self.score}/{self.total_questions} です！")
            return

        # 正しい回答を選択
        self.current_word = random.choice([word for word in quiz_data.keys() if word not in self.questions_asked])
        self.questions_asked.append(self.current_word)
        self.correct_answer = quiz_data[self.current_word]

        # 問題を表示
        self.label_word.config(text=f"フランス語: {self.current_word}")
        self.entry_answer.delete(0, tk.END)
        self.label_feedback.config(text="")

    def check_answer(self):
        # ユーザーの回答を取得
        user_answer = self.entry_answer.get().strip()
        if user_answer.lower() == self.correct_answer.lower():
            self.label_feedback.config(text="正解！", fg="green")
            self.score += 1
        else:
            self.label_feedback.config(text=f"不正解！ 正しい回答: {self.correct_answer}", fg="red")
        
        # スコア更新
        self.label_score.config(text=f"現在のスコア: {self.score}/{self.total_questions}")
        self.next_question()

    def restart_quiz(self):
        # クイズをリセット
        self.score = 0
        self.questions_asked = []
        self.label_score.config(text=f"現在のスコア: {self.score}/{self.total_questions}")
        self.next_question()

# アプリの実行
if __name__ == "__main__":
    root = tk.Tk()
    app = FrenchQuizApp(root)
    root.mainloop()
