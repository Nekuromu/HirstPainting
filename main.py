from turtle import Turtle, Screen
from random import choice

color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176),
              (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49),
              (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86),
              (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162),
              (156, 212, 190), (87, 46, 33), (37, 45, 83)]

turt = Turtle()
turt.speed("fastest")
Screen().colormode(255)
turt.hideturtle()


# 10 x 10
# 50 paces apart

def make_hirst_painting(width, height):
    turt.penup()
    turt.setx(-(48 * (width / 2)))
    turt.sety(-(40 * (height / 2)))
    for row in range(0, height):
        for column in range(0, width):
            turt.dot(25, choice(color_list))
            turt.penup()
            turt.forward(50)
        turt.backward(width * 50)
        turt.sety(turt.ycor() + 50)


make_hirst_painting(10, 10)

screen = Screen()
screen.exitonclick()
