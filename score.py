from turtle import Turtle,Screen

screen = Screen()
screen.bgcolor('black')
turtle = Turtle()
turtle.hideturtle()

turtle.color('white')
turtle.penup()
turtle.goto(x=0,y=280)
turtle.pendown()

turtle.write("Score is", align='center')

















screen.exitonclick()