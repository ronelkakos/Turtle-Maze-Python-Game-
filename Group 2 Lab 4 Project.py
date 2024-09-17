import turtle
import random
import time


#Ronel (did the code)
#Creating four random background colors for every time you play the maze game
#Single loop
def randombgcolor():
    bgcolorslist = ["orange", "magenta", "purple", "gray"]
    for i in range (1):
        bgcolors = random.choice(bgcolorslist)
        turtle.bgcolor(bgcolors)
    return bgcolors
        
    

#Jack, Ronel, Carson, and Syed (all together we did the maze drawing code)
#We all were assigned a specific corner of the maze in order to draw it out,
#and we combined it all together on the movementdraw() function so that it
#can draw the whole maze fully.

#Ronel and Carson (did the nested loop random maze line color)
#Carson was able to base out the nested loop and Ronel was able to work it
#out and be able to get the colors working on changing.
def movementdraw():
    for count in range(1):
        linecolorlist = ["red","blue","yellow","green","cyan","brown"]
        random.shuffle(linecolorlist)
        for count in range(1, len(linecolorlist)):
            turtle.pencolor(linecolorlist[count])
        #Ronel portion
        turtle.speed(5)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.pensize(5)
        turtle.pencolor(linecolorlist[count])
        turtle.left(180)
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(225)
        turtle.left(90)
        turtle.forward(150)
        turtle.penup()
        turtle.goto(-150, -225)
        turtle.pendown()
        turtle.right(180)
        turtle.forward(75)
        turtle.right(90)
        turtle.forward(225)
        turtle.penup()
        turtle.goto(-75, -75)
        turtle.pendown()
        turtle.right(180)
        turtle.forward(75)
        turtle.left(90)
        turtle.forward(75)
        turtle.penup()
        #Jack portion
        turtle.goto(-75, 225)
        turtle.pendown()
        turtle.goto(-225, 225)
        turtle.penup()
        turtle.goto(-225, 0)
        turtle.pendown()
        turtle.goto(-225, 225)
        turtle.penup()
        turtle.goto(-150, 0)
        turtle.pendown()
        turtle.goto(-150, 150)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.goto(-150, 0)
        turtle.penup()
        turtle.goto(0, 75)
        turtle.pendown()
        turtle.goto(0, 0)
        turtle.penup()
        turtle.goto(-75, 75)
        turtle.pendown()
        turtle.goto(0, 75)
        turtle.penup()
        turtle.goto(-75, 150)
        turtle.pendown()
        turtle.goto(-75, 75)
        turtle.penup()
        turtle.goto(225,0)
        #Carson portion
        turtle.goto(225,0)
        turtle.pendown()
        turtle.setheading(180)
        turtle.forward(75)
        turtle.penup()
        turtle.setheading(270)
        turtle.forward(75)
        turtle.pendown()
        turtle.forward(75)
        turtle.setheading(90)
        turtle.forward(75)
        turtle.setheading(180)
        turtle.forward(75)
        turtle.setheading(90)
        turtle.forward(75)
        turtle.setheading(270)
        turtle.forward(75)
        turtle.setheading(180)
        turtle.forward(75)
        turtle.setheading(90)
        turtle.forward(75)
        turtle.penup()
        turtle.goto(225,0)
        turtle.pendown()
        turtle.setheading(270)
        turtle.forward(225)
        turtle.setheading(180)
        turtle.forward(150)
        turtle.setheading(90)
        turtle.forward(75)
        turtle.setheading(180)
        turtle.forward(75)
        turtle.penup()
        #Syed portion
        turtle.goto(0, 225)
        turtle.pendown()
        turtle.goto(225,225)
        turtle.penup()
        turtle.goto(225,0)
        turtle.pendown()
        turtle.goto(225,225)
        turtle.penup()
        turtle.goto(150,225)
        turtle.pendown()
        turtle.goto(150,75)
        turtle.penup()
        turtle.goto(75,150)
        turtle.pendown()
        turtle.goto(75,0)
        turtle.penup()
        turtle.goto(225,0)
        turtle.pendown()
        turtle.goto(150,0)
        turtle.penup()
        turtle.goto(0,75)
        turtle.pendown()
        turtle.goto(0,0)
        turtle.penup()
        turtle.goto(0,225)
        turtle.pendown()
        turtle.goto(0,150)
        turtle.penup()
        turtle.goto(-37.5, 235)

#Carson (did the code)
#The randomcursor() function involves a set of six different cursor shapes
#that the user can decide to choose from before they start playing the maze
#game.
def randomcursor():

    screen = turtle.Screen()
    cursor = screen.textinput("Choose Cursor", "classic, arrow, turtle, circle, square, or triangle:")
    
    if cursor == "classic":
        turtle.shape("classic")
    elif cursor == "arrow":
        turtle.shape("arrow")
    elif cursor == "turtle":
        turtle.shape("turtle")
    elif cursor == "circle":
        turtle.shape("circle")
    elif cursor == "square":
        turtle.shape("square")
    elif cursor == "triangle":
        turtle.shape("triangle")

    turtle.shape(cursor)
    return turtle

#Jack (did the code)
#In these functions below, they are moving the turtle functions with
#every coordinate of movement so that it can take in every xcor and ycor.
def moving_forward():
    turtle.forward(5)
    xcor = turtle.xcor()
    ycor = turtle.ycor()
    coordinateswallblock(xcor, ycor)
    checkwin(xcor, ycor)
def moving_backward():
    turtle.backward(5)
    xcor = turtle.xcor()
    ycor = turtle.ycor()
    coordinateswallblock(xcor, ycor)
    checkwin(xcor, ycor)
def moving_right():
    turtle.right(90)
    xcor = turtle.xcor()
    ycor = turtle.ycor()
    
def moving_left():
    turtle.left(90)
    xcor = turtle.xcor()
    ycor = turtle.ycor()
    

#Ronel (did the code)
#In the windowscreen() function, this displays the window screen for the maze
#and it allows the user to be able to use keystrokes on the keyboard in order
#to move their cursor through the maze game. 
def windowscreen():
    window = turtle.Screen()
    window.listen()
    window.onkeypress(moving_forward, "Up")
    window.onkeypress(moving_backward, "Down")
    window.onkeypress(moving_right, "Right")
    window.onkeypress(moving_left, "Left")
    return window

#Carson (did the code)
#In the coordinateswallblock(x, y) function, there is a random color cursor
#created so that for every movement the cursor is making throughout the
#maze, the color of the cursor changes everytime.
def coordinateswallblock(x, y):
    cursorcolor = ["red","blue","yellow","green","cyan","brown"]

    rannum1 = random.randint(0,len(cursorcolor))

    if rannum1 == 0:
        turtle.pencolor("red")
    elif rannum1 == 1:
        turtle.pencolor("blue")
    elif rannum1 == 2:
        turtle.pencolor("yellow")
    elif rannum1 == 3:
        turtle.pencolor("green")
    elif rannum1 == 4:
        turtle.pencolor("cyan")
    elif rannum1 == 5:
        turtle.pencolor("brown")

    fillcolor = ["red","blue","yellow","green","cyan","brown"]

    rannum2 = random.randint(0,len(fillcolor))

    if rannum2 == 0:
        turtle.fillcolor("red")
    elif rannum2 == 1:
        turtle.fillcolor("blue")
    elif rannum2 == 2:
        turtle.fillcolor("yellow")
    elif rannum2 == 3:
        turtle.fillcolor("green")
    elif rannum2 == 4:
        turtle.fillcolor("cyan")
    elif rannum2 == 5:
        turtle.fillcolor("brown")

#Jack, Carson, Ronel, and Syed (did the code of each maze portion wall coordin.)
#Making sure the turtle resets position when running into the maze walls.   
    if -230 < x < -220 and -230 < y < 230:
        turtle.goto(-37.5,235)
    elif -230 < x < -70 and 220 < y < 230:
        turtle.goto(-37.5,235)
    elif -5 < x < 230 and 220 < y < 230:
        turtle.goto(-37.5, 235)
    elif 145 < x < 155 and 70 < y < 230:
        turtle.goto(-37.5, 235)
    elif 145 < x < 230 and -5 < y < 5:
        turtle.goto(-37.5, 235)
    elif 220 < x < 230 and -230 < y < 230:
        turtle.goto(-37.5, 235)
    elif -5 < x < 5 and 145 < y < 230:
        turtle.goto(-37.5, 235)
    elif -5 < x < 5 and -80 < y < 80:
        turtle.goto(-37.5, 235)
    elif 70 < x < 80 and -80 < y < 155:
        turtle.goto(-37.5, 235)
    elif -5 < x < 155 and -80 < y < -70:
        turtle.goto(-37.5, 235)
    elif 145 < x < 155 and -155 < y < -70:
        turtle.goto(-37.5, 235)
    elif 70 < x < 230 and -230 < y < -220:
        turtle.goto(-37.5, 235)
    elif -230 < x < 5 and -230 < y < -220:
        turtle.goto(-37.5, 235)
    elif -155 < x < -145 and -230 < y < 155:
        turtle.goto(-37.5, 235)
    elif -80 < x < -70 and -155 < y < -70:
        turtle.goto(-37.5, 235)
    elif -80 < x < -70 and 70 < y < 155:
        turtle.goto(-37.5, 235)
    elif 70 < x < 80 and -230 < y < -145:
        turtle.goto(-37.5, 235)
    elif -80 < x < 80 and -155 < y < -145:
        turtle.goto(-37.5, 235)
    elif -155 < x < 5 and -5 < y < 5:
        turtle.goto(-37.5, 235)
    elif -80 < x < 5 and 70 < y < 80:
        turtle.goto(-37.5, 235)
    elif -5 < x < 5 and 225 < y < 300:
        turtle.goto(-37.5, 235)
    elif -80 < x < -70 and 225 < y < 300:
        turtle.goto(-37.5, 235)
    

#Jack and Syed (did the code)
#Jack did coordinates of checkwin() function along with the couple
#turtle movements. Syed added the messages of turtle.write to make sure
#it'll display that the user won and a thank you message with the time.sleep()
#function.
def checkwin(x, y):
    if 0 < x < 75 and -240 < y < -225:
        window = turtle.Screen()
        turtle.penup()
        turtle.clear()
        turtle.hideturtle()
        turtle.goto(0,0)
        turtle.write("Winner!", align="center", font=('Normal', 30))
        time.sleep(3)
        turtle.goto(0,0)
        turtle.clear()
        turtle.hideturtle()
        turtle.write("Thanks for Playing!", align = "center", font = ("Normal", 30))
        time.sleep(5)
        turtle.clear()
        turtle.bye()
        
        

def main():
    randombgcolor()
    movementdraw()
    randomcursor()
    windowscreen()
    xcor = turtle.xcor()
    ycor = turtle.ycor()
    coordinateswallblock(xcor, ycor)

main()
