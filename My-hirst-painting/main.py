hirsts_color = [(173, 79, 33), (240, 224, 82), (47, 35, 25), (214, 151, 86), (149, 26, 40), (22, 25, 66), (43, 44, 119), (165, 22, 15), (52, 87, 152), (208, 85, 126), (125, 162, 216), (151, 53, 85), (27, 42, 28), (215, 79, 61), (142, 182, 144), (113, 106, 199)]

import random
import turtle as turtle_module

tim = turtle_module.Turtle()

turtle_module.colormode(255)

screen = turtle_module.Screen()
def paint_a_row():
    for n in range(10):
        dots_color = random.choice(hirsts_color)
        tim.dot(20, dots_color)
        tim.penup()
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

tim.penup()
tim.setheading(270)
tim.forward(200)
tim.setheading(0)
tim.pendown()
for n in range(10):
        paint_a_row()






screen.exitonclick()