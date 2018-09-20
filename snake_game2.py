import turtle


#set up the screen
wn= turtle.Screen()
wn.bgcolor("lightgreen")

#draw border
mypen= turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
mypen.pendown()
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()





#create player turtle
player= turtle.Turtle()
player.color("red")
player.shape("triangle")
#removing the trail by penup
player.penup()
#speed of animation and nt of movement
player.speed(0)

#set speed variable
speed=1


#define function
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increase_speed():
    global speed
    speed+=1

#set keyboaed binding
#once set it automatically does that no need for a loop where
#direction is stated
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increase_speed, "Up")
while 1:
    player.forward(speed)
    #boundary_check
    if player.xcor()>300:
        player.goto(-300,player.ycor())

    if player.xcor() < -300:
        player.goto(300,player.ycor())

    if player.ycor()>300 :
        player.goto(player.xcor(),-300)

    if player.ycor()<-300:
        player.goto(player.xcor(),300)




