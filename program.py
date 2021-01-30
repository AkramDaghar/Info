from turtle import *

shape("turtle")
speed(1)
pensize(1)
pencolor("black")

x = 0
while x in range(0, 650):
    x += 50;
    forward(x)
    left(120)

"""

# the following code will give the same output as the previous one

forward(50)
left(120)
forward(100)
left(120)
forward(150)
left(120)
forward(200)
left(120)
forward(250)
left(120)
forward(300)
left(120)
forward(350)
left(120)
forward(400)
left(120)
forward(450)
left(120)
forward(500)
left(120)
forward(550)
left(120)
forward(600)
left(120)
forward(650)
left(120)
"""