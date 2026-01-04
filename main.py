from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10 # tim.left(10)
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10 # tim.right(10)
    tim.setheading(new_heading)

screen.listen()
screen.onkey(move_forwards, "g")
screen.onkey(move_backwards, "i")
screen.onkey(turn_left, "u")
screen.onkey(turn_right, "e")
screen.exitonclick()