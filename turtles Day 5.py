import turtle

t=turtle.Turtle()

def circle(size):
    circle_1 = 0
    while circle_1 < 120:
        t.forward(size)
        t.left(3)
        circle_1 = circle_1 + 1

circle(5)
t.left(90)
t.penup()
t.forward(20)
t.right(90)
t.pendown()
circle(4)
t.left(90)
t.penup()
t.forward(45)
t.pendown()
t.right(90)
circle(1)
t.penup()
t.goto(0,190)
t.pendown()
t.left(90)
t.forward(50)
t.right(90)

def semicircle(size):
    semicircle_1 = 0
    while semicircle_1 < 60
    t.forward(size)
        t.left(3)
        semicircle_1 = semicircle_1 + 1

semicircle(7)

input()
