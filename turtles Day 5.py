import turtle

t=turtle.Turtle()
t.speed(0)

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

def rightsemicircle(size):
    rightsemicircle_1 = 0
    while rightsemicircle_1 < 60:
        t.forward(size)
        t.right(3)
        rightsemicircle_1 = rightsemicircle_1 + 1

def leftsemicircle(size):
    leftsemicircle_1 = 0
    while leftsemicircle_1 < 60:
        t.forward(size)
        t.left(3)
        leftsemicircle_1 = leftsemicircle_1 + 1

rightsemicircle(7)
leftsemicircle(1)
leftsemicircle(8.1)
t.goto(0,240)


input("enter the truth of the world to exit")
