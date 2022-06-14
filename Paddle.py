from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class Computer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.goto(x=410, y=0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move(self):
        self.speed('slow')
        move = True
        while move:
            while self.ycor() < 320:
                self.forward(20)

            while self.ycor() > -320:
                self.backward(20)