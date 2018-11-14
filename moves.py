import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    for x in range (0,4):
        brad.forward(100)
        brad.right(90)
        x + 1


    window.exitonclick()
draw_square()
