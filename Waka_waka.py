#Authors: Rune

#Summon turtle
import turtle
import random

turtle.hideturtle()


#Named constant
SCREEN_WIDTH= 800
SCREEN_HEIGHT = 800

#Make background
wn = turtle.Screen()
wn.bgcolor("dark blue")

# Game Title
wn.title("Waka waka")

#Make a maze


#PizzaMan

#Pacman gif as turtle go!
screen = turtle.Screen()
screen.register_shape('Pizzaman.gif')

# taking input for the radius of the circle
pizza = turtle.Turtle()
pizza.shape('Pizzaman.gif')
pizza.color('yellow')
pizza.speed(0)
pizza.penup()
pizza.speed(0)
pizza.width(5)

#Define directions
def up ():
    pizza.setheading(90)
    pizza.forward(5)


def down ():
    pizza.setheading(270)
    pizza.forward(5)

def left ():
    pizza.setheading(180)
    pizza.forward(5)

def right ():
    pizza.setheading(0)
    pizza.forward(5)

#Input and receive instructions
turtle.listen()

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')


turtle.mainloop()