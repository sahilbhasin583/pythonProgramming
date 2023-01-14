import turtle

turtle.pensize(5)
turtle.pencolor("black")
turtle.begin_fill()
turtle.fillcolor("yellow")

turtle.back(50)
turtle.right(120)
turtle.back(100)
turtle.right(150)
turtle.back(86)
turtle.end_fill()

turtle.begin_fill()
turtle.fillcolor("green")

turtle.right(90)
turtle.forward(50)
turtle.left(120)
turtle.forward(100)
turtle.end_fill()
turtle.hideturtle()
turtle.done()