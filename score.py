from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(-100, 240)
        self.write(f"{self.l_score}", font=("Arial", 40, "normal"))
        self.goto(100, 240)
        self.write(f"{self.r_score}", font=("Arial", 40, "normal"))

    def left_score(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def right_score(self):
        self.clear()
        self.r_score += 1
        self.update_score()
