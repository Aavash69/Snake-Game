from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.color('white')
        self.score = 0
        self.highscore = 0
        self.goto(x=0, y=280)
        self.change_score()

    def eats(self):
        self.score += 1
        self.clear()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.goto(x=0,y=0)

        self.write(f"Game Over", align="center", font=('Arial', 14, 'normal'))

    def change_score(self):
        self.write(f"Current Score: {self.score}. High Score: {self.highscore}", align="center", font=('Arial', 14, 'normal'))



