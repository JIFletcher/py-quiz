from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Label Score
        self.lbl_score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.lbl_score.grid(row=0, column=1)
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        # Canvas Question Text
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some kind of question?",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Button True
        self.true_btn_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=self.true_btn_img, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(row=2, column=0)
        # Button False
        self.false_btn_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=self.false_btn_img, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(row=2, column=1)
        # Get the next question
        self.get_next_question()
        # Window mainloop
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.lbl_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.true_btn.config(state="normal")
            self.false_btn.config(state="normal")
        else:
            self.canvas.itemconfig(self.question_text, text=f"Quiz is done.\nFinal score: {self.quiz.score} / 10")

    def true_pressed(self):
        self.true_btn.config(state="disabled")
        self.false_btn.config(state="disabled")
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        self.true_btn.config(state="disabled")
        self.false_btn.config(state="disabled")
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

