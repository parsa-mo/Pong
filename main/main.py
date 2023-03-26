import time
from turtle import Screen
from Scoreboard import Line, P1, P2
from Paddle import Paddle
from Ball import Ball

screen = Screen()
screen.setup(width=900, height=700)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

line = Line()
left_player_score = P1()
right_player_score = P2()

r_paddle = Paddle((410, 0))
l_paddle = Paddle((-410, 0))

ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect ball collision with the wall
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.wall_bounce()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 395:
        ball.paddle_bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -395:
        ball.paddle_bounce()

    # Right paddle misses
    if ball.xcor() > 440:
        ball.reset()
        right_player_score.update()

    if ball.xcor() < -440:
        ball.reset()
        left_player_score.update()



screen.exitonclick()
