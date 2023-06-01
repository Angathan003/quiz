import tkinter as tk

quiz_data = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "London", "Berlin", "Rome"],
        "correct_answer": 0
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answers": ["Mars", "Venus", "Mercury", "Jupiter"],
        "correct_answer": 0
    },
    {
        "question": "Who painted the Mona Lisa?",
        "answers": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
        "correct_answer": 0
    }
]


class QuizApplication:
    def __init__(self, master):
        self.master = master
        self.questions = quiz_data
        self.current_question = 0
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text="Question")
        self.question_label.pack()

        self.answer_var = tk.IntVar()
        self.answers_radios = []
        for i in range(4):
            answer_radio = tk.Radiobutton(
                self.master,
                variable=self.answer_var,
                value=i
            )
            answer_radio.pack()
            self.answers_radios.append(answer_radio)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_answer)
        self.submit_button.pack()

        self.next_button = tk.Button(self.master, text="Next", state=tk.DISABLED, command=self.next_question)
        self.next_button.pack()

    def start(self):
        self.show_question()

    def show_question(self):
        question_data = self.questions[self.current_question]
        question = question_data['question']
        answers = question_data['answers']

        self.question_label.config(text=question)
        for i, answer_radio in enumerate(self.answers_radios):
            answer_radio.config(text=answers[i])

    def submit_answer(self):
        question_data = self.questions[self.current_question]
        correct_answer = question_data['correct_answer']
        selected_answer = self.answer_var.get()

        if selected_answer == correct_answer:
            self.score += 1

        self.next_button.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.DISABLED)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
            self.next_button.config(state=tk.DISABLED)
            self.submit_button.config(state=tk.NORMAL)
        else:
            self.show_result()

    def show_result(self):
        question_data = self.questions[self.current_question - 1]
        correct_answer_index = question_data['correct_answer']
        correct_answer = question_data['answers'][correct_answer_index]

        self.question_label.config(text=f"Quiz Completed! Your score: {self.score}/{len(self.questions)}")
        self.submit_button.pack_forget()
        self.next_button.pack_forget()

        correct_answer_label = tk.Label(self.master, text=f"Correct answer: {correct_answer}")
        correct_answer_label.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Quiz Application")
    quiz_app = QuizApplication(root)
    quiz_app.start()
    root.mainloop()
