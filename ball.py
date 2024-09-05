from turtle import Turtle
ORIGIN = (0, 0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(ORIGIN)
        self.bounce_x()

    def increase_speed(self):
        if self.y_move > 0:
            self.y_move += 2
        else:
            self.y_move -= 2
        if self.x_move > 0:
            self.x_move += 2
        else:
            self.x_move -= 2

    def reset_speed(self):
        if self.y_move > 0:
            self.y_move = 10
        else:
            self.y_move = -10
        if self.x_move > 0:
            self.x_move = 10
        else:
            self.x_move = -10
