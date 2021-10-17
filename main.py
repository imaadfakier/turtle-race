from turtle import Turtle, Screen
import random

screen = Screen()
# (event) listening for events; keystrokes, mouse clicks, window resizing etc.
screen.listen()


# binding a keystroke to an event; implementing an event listener
# def move_forwards():
#     turtle.forward(10)
#
#
# the idea of a higher order function is a function that can work with other
# functions; in this case, the onkey method is a higher order function because
# it takes or, rather, expects another function to be passed as an argument
# where the passed function is interacted with or used in its implementation
# screen.onkey(
#     # fun=move_forwards(), # not done when passing functions
#     fun=move_forwards,
#     key='space'
# )

# --- ETCH-A-SKETCH PROJECT ---
# def go_forward():
#     turtle.forward(10)
#
#
# screen.onkey(
#     fun=go_forward,
#     key='w'
# )
#
#
# def go_backward():
#     turtle.backward(10)
#
#
# screen.onkey(
#     fun=go_backward,
#     key='s'
# )
#
#
# def turn_left():
#     # turtle.left(45)
#     # turtle.setheading(turtle.heading() + 10)
#     turtle.left(10)
#
#
# screen.onkey(
#     fun=turn_left,
#     key='a'
# )
#
#
# def turn_right():
#     # turtle.right(45)
#     # turtle.setheading(turtle.heading() - 10)
#     turtle.right(10)
#
#
# screen.onkey(
#     fun=turn_right,
#     key='b'
# )
#
#
# def erase_drawing():
#     # screen.clearscreen()
#     # screen.clear()
#     turtle.clear()
#     turtle.penup()
#     turtle.home()
#     turtle.pendown()
#
#
# screen.onkey(
#     fun=erase_drawing,
#     key='c'
# )
#
# turtle = Turtle()

# --- TURTLE RACE GAME ---
turtles = []
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_coordinate = -100

# screen.setup(500, 400)
screen.setup(width=500, height=400)  # readability! Readability! Readability!
user_bet = screen.textinput(title='Make Your Bet', prompt='Which turtle will win the race? Enter a color: ')
# print(user_bet)

# turtle = Turtle()
# turtle.shape('turtle')
# turtle = Turtle(shape='turtle')
# turtle.penup()
# turtle.goto(x=-230, y=-100)
for i in range(6):
    turtles.append(Turtle(shape='turtle'))
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].goto(x=-230, y=y_coordinate)
    # y_coordinate += 25
    y_coordinate += 30

while user_bet:
    for the_turtle in turtles:
        if the_turtle.xcor() >= 230:
            # print(the_turtle.color())
            winning_color = the_turtle.fillcolor()
            # winning_color = the_turtle.pencolor()
            if user_bet == winning_color:
                print(f'You\'ve won! The {winning_color} turtle is the winner!')
            else:
                print(f'You\'ve lost! The {winning_color} turtle is the winner!')
            user_bet = ''
        if not user_bet:
            break

        the_turtle.forward(random.randint(0, 9))

screen.exitonclick()
