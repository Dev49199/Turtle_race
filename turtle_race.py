import turtle
from random import randint

ts=turtle.Screen()

tur2=turtle.Turtle()
tur2.hideturtle()
tur=turtle.Turtle()
tur.hideturtle()
tur3=turtle.Turtle()
tur3.hideturtle()
screen=turtle.Turtle()
screen.hideturtle()

def start_screen():
    
    screen.penup()
    screen.goto(-130,130)
    screen.write("Welcome to turtle game",font=('Arial',20,'normal'))
    screen.goto(-100,10)
    screen.write("Press s to start!!!",font=('Arial',10,'normal'))


def game():
    turtle.Screen().clear()
    tur2=turtle.Turtle()
    tur=turtle.Turtle()
    tur.hideturtle()
    tur3=turtle.Turtle()
    tur.speed(10)
    tur.penup()
    tur.goto(-140,140)
    for step in range(16):
    	tur.write(step,align='center')
    	tur.right(90)
    	tur.forward(10)
    	tur.pendown()
    	tur.forward(150)
    	tur.penup()
    	tur.backward(160)
    	tur.left(90)
    	tur.forward(20)  
   
    tur2.color('red')
    tur2.shape('turtle')
    tur2.penup()
    tur2.goto(-160,100)
    tur2.pendown()

   
    tur3.color('blue')
    tur3.shape('turtle')
    tur3.penup()
    tur3.goto(-160,70)
    tur3.pendown()
    tur.goto(-200,-80)
    tur.write('Press w to start')
    
    def start_race():
        for turn in range(100):
            tur2.forward(randint(1,6))
            tur3.forward(randint(1,6))


    ts.onkey(start_race,'w')
    ts.listen()
     

    






#print(tur.pos())
start_screen()
ts.onkey(game,'s')
ts.listen()

turtle.done()
