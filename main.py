from tkinter import PhotoImage
from turtle import Screen, Turtle, Shape

from PIL import Image, ImageTk

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

from target import Target

screen = Screen()
screen.bgcolor("black")
width = 50
height = 50
start_x = -350
start_y = +200

# larger = PhotoImage(file="watermark.gif").r(1, 1)
img = ImageTk.PhotoImage(Image.open("breaks.png").resize((width, height)))
screen.addshape("img", Shape("image", img))
# screen.addshape('watermark.gif')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

target_objects = []

target = Target(target_number=45,
                start_x=start_x,
                start_y=start_y,
                img_width=width,
                img_height=height,
                lenght=15)
target.my_shape(path="img")
target_objects = target.display()

# for index in range(len(target_objects)):
#     if index % 10 == 0:
#         target_objects[index].hideturtle()
#     print(target_objects[index].xcor(), target_objects[index].ycor())


# for index in range(len(target_objects)):
#     if not index:
#         start_x = start_x
#     elif index % 15 == 0:
#         start_y -= height + 2
#         start_x = -350
#     else:
#         start_x += width
#     target_objects[index].goto(start_x, start_y)


paddle = Paddle((0, -250))
ball = Ball()
ball.my_shape("circle")
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True
closest_objet = paddle
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280:
        ball.bounce_y()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    for objet in target_objects:
        if ball.distance(objet) < 50:
            ball.bounce_y()
            objet.hideturtle()
            scoreboard.point()
            target_objects.remove(objet)
            break
    # Detect collision with paddle
    if abs(ball.xcor() - paddle.xcor()) < 76 and abs(ball.ycor() - paddle.ycor()) < 20:
        print(ball.ycor())
        ball.bounce_y()

    # Detect R paddle misses
    if ball.ycor() < -320:
        ball.reset_position()
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
