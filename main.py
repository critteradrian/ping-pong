from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen_titles = ["ping!", "pong!"]
screen_title = 0


def change_title():
    global screen_titles
    global screen_title
    if screen_title == 0:
        screen_title += 1
        screen.title(screen_titles[screen_title])
    else:
        screen_title -= 1
        screen.title(screen_titles[screen_title])


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title(screen_titles[screen_title])
screen.tracer(0)

scoreboard = Scoreboard()

ball = Ball()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
        change_title()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.increase_speed()
        ball.bounce_x()
        change_title()

    if ball.xcor() > 400:
        ball.reset_position()
        ball.reset_speed()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_position()
        ball.reset_speed()
        scoreboard.r_point()

screen.exitonclick()
