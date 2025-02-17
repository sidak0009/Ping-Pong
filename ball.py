from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_Speed=0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_Speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_Speed = 0.1
        self.bounce_paddle()
