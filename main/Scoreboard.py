from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.create_line()

    def create_line(self):
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=-330)
        self.setheading(90)
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.shape('square')
        self.color('white')

        while self.ycor() < 350:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)


class P1(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x=-70, y=280)
        self.write(arg=self.score, move=False, align='center', font=('SquareFont', 35, 'bold'))

    def update(self):
        self.score += 1
        self.clear()
        self.write(arg=self.score, move=False, align='center', font=('SquareFont', 35, 'bold'))


class P2(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x=70, y=280)
        self.write(arg=self.score, move=False, align='center', font=('SquareFont', 35, 'bold'))

    def update(self):
        self.score += 1
        self.clear()
        self.write(arg=self.score, move=False, align='center', font=('SquareFont', 35, 'bold'))