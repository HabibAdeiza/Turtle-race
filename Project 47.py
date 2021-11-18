import turtle
import random

#Background
bg = turtle.Screen()
bg.bgcolor("blue")
bg.title("Turtle racing game!")

#Colors
colors = ["red", "white", "green", "yellow", "black"]
turtle_list = []

#Tracks
def Tracks(x, y):
    track = turtle.Turtle()
    track.pu()
    track.goto(x, y)
    track.ht()
    for i in range(25):
        track.pencolor("black")
        track.fd(50)
        track.pu()
        track.fd(50)
        track.pd()
bg.tracer(0)
Tracks(-1100, 300)
Tracks(-1100, 200)
Tracks(-1100, 100)
Tracks(-1100, 0)
Tracks(-1100, -100)
Tracks(-1100, -200)
bg.tracer(1)

#Finish line
def Finish_line():
    Finish = turtle.Turtle()
    Finish.pu()
    Finish.pensize(20)
    Finish.goto(900, -500)
    Finish.pd()
    Finish.pencolor("brown")
    Finish.lt(90)
    Finish.fd(1100)
bg.tracer(0)
Finish_line()
bg.tracer(1)

#Movement of turtles
posx = -800
posy = 240

bg.tracer(0)
for i in range(5):
    players = turtle.Turtle()
    players.shape("turtle")
    players.color(colors[i])
    players.pu()
    players.goto(posx ,posy)
    posy -= 100
    turtle_list.append(players)
bg.tracer(1)

game_on = True
while game_on:
    for i in range(5):
         if turtle_list[i].xcor() >= 900:
             winner = (colors[i])
             text = turtle.Turtle()
             text.pu()
             text.ht()
             text.goto(0, 0)
             text.color(winner)
             text.write(f"{winner} is the winner" ,  False,  align = "center", font = ('Arial', 100, 'normal'))
             game_on = False
         turtle_list[i].fd(random.randint(1,10))





            
