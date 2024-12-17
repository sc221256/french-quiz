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
        self.root.configure(bg="#d3d3d3")  # 背景色をグレーに変更
        self.score = 0
        self.questions_asked = []
        self.total_questions = len(quiz_data)
        self.current_word = ""
        self.correct_answer = ""

        # クラシックフレーム
        self.frame_main = tk.Frame(root, bd=10, relief="ridge", bg="#ffffff")
        self.frame_main.pack(padx=20, pady=20)

        # リボンを追加するためのキャンバス
        self.canvas_ribbon = tk.Canvas(self.frame_main, width=500, height=30, bg="#ffffff", highlightthickness=0)
        self.canvas_ribbon.pack(pady=5)
        self.canvas_ribbon.create_rectangle(0, 5, 500, 25, fill="#d4af37", outline="")  # 金色のリボン

        # タイトルのフレーム
        self.frame_title = tk.Frame(self.frame_main, bg="#ffffff")
        self.frame_title.pack(pady=10)

        # フランスの国旗色を適用
        self.label_title_blue = tk.Label(self.frame_title, text="フラ", font=("Helvetica", 16, "bold"), fg="blue", bg="#ffffff")
        self.label_title_white = tk.Label(self.frame_title, text="ンス語", font=("Helvetica", 16, "bold"), fg="black", bg="#ffffff")  # 色を黒に変更
        self.label_title_red = tk.Label(self.frame_title, text="クイズ", font=("Helvetica", 16, "bold"), fg="red", bg="#ffffff")
        
        self.label_title_blue.pack(side="left")
        self.label_title_white.pack(side="left")
        self.label_title_red.pack(side="left")

        self.label_word = tk.Label(self.frame_main, text="", font=("Helvetica", 14), bg="#ffffff")
        self.label_word.pack(pady=10)

        self.entry_answer = tk.Entry(self.frame_main, font=("Helvetica", 14))
        self.entry_answer.pack(pady=10)

        self.button_submit = tk.Button(self.frame_main, text="答える", command=self.check_answer)
        self.button_submit.pack(pady=5)

        self.label_feedback = tk.Label(self.frame_main, text="", font=("Helvetica", 12), bg="#ffffff")
        self.label_feedback.pack(pady=5)

        self.label_score = tk.Label(self.frame_main, text=f"現在のスコア: {self.score}/{self.total_questions}", font=("Helvetica", 12), bg="#ffffff")
        self.label_score.pack(pady=10)

        self.button_restart = tk.Button(self.frame_main, text="再挑戦", command=self.restart_quiz)
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
