from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Pong')

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Score()

# screen.tracer(1)

screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -275:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 45 and ball.xcor() > 320) or (ball.distance(l_paddle) < 45 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 345:
        ball.reset_position()
        score.left_score()
    if ball.xcor() < -345:
        ball.reset_position()
        score.right_score()

screen.exitonclick()
