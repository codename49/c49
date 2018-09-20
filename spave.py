import turtle
import math
import random
import os

#set up the screen
wn= turtle.Screen()
wn.bgcolor("white")
wn.bgpic("/root/Downloads/stars.gif")
wn.tracer(2)

#draw border
mypen= turtle.Turtle()
mypen.penup()
mypen.setposition(-400,-300)
mypen.pendown()
mypen.pensize(3)
mypen.pendown()
mypen.forward(800)
mypen.left(90)
mypen.forward(600)
mypen.left(90)
mypen.forward(800)
mypen.left(90)
mypen.forward(600)
mypen.hideturtle()
score= 0


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


#create goals
max_goal=6
goals=[]
for i in range(max_goal):
    goals.append(turtle.Turtle())
    goals[i].color("pink")
    goals[i].penup()
    goals[i].speed(0)
    goals[i].shape("circle")
    goals[i].setposition(random.randint(-400,400), random.randint(-300,300))




#define function
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increase_speed():
    global speed
    speed+=1

def iscollision(t1, t2):
    d= math.sqrt(math.pow(t1.xcor()- t2.xcor(), 2)+ math.pow(t1.ycor()-t2.ycor(),2))
    if d< 20:
        return True
    else:
        return False



#set keyboaed binding
#once set it automatically does that no need for a loop where
#direction is stated
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increase_speed, "Up")
while 1:
    player.forward(speed)
    #xboundary_check
    if player.xcor()>400 or player.xcor()<-400:
        player.right(180)
    #ybcheck
    if player.ycor()>300 or player.ycor()<-300:
        player.right(180)




    for i in range(max_goal):

        #movement_goal
        goals[i].forward(3)

        #goalbxcheck
        if goals[i].xcor()>390 or goals[i].xcor()<-390:
            goals[i].right(180)
        # goalbxcheck
        if goals[i].ycor()>290 or goals[i].ycor()<-290:
            goals[i].right(180)

        #collison checking
        if iscollision(player, goals[i]):
            goals[i].setposition(random.randint(-288,288), random.randint(-288,288))
            goals[i].right(random.randint(0, 360))
            if score>3:
                score+=2
                speed+=1
            else:
                score+=1

            # print(score)
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            score_str = "score:%s " % score
            mypen.write(score_str, False, align="left", font=("Arial", 16, "bold"))

delay= input("press Enter to finish")