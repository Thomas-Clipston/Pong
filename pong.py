from cProfile import label
from cgitb import text
from glob import glob
from textwrap import fill
import tkinter as tk
from turtle import bgcolor, color
from click import command
import random

cordx = 35
cordy = 110
cordxx = 450
cordyy = 110

ballx = 240
bally = 240
autox = 5
autoy = 0
score1track = 0
score2track = 0

window = tk.Tk()
window.geometry("500x500")
window.resizable(width=False, height=False)

myCanvas = tk.Canvas(window, bg="black", height=500, width=500)
myCanvas.pack()
#paddles
block1 = myCanvas.create_rectangle(cordx,cordy,cordx+20,cordy+110,fill="white")
block2 = myCanvas.create_rectangle(cordxx,cordyy,cordxx+20,cordyy+110,fill="white")
#little bit of desighn elements
middleline = myCanvas.create_line(250,0,250,500, fill="white",dash=(5,3))
score1 = myCanvas.create_text(210,30,text=0,font="Times 30",fill="white")
score2 = myCanvas.create_text(290,30,text=0,font="Times 30",fill="white")
#ball
ball = myCanvas.create_rectangle(ballx,bally,ballx+20,bally+20,fill="green")

#moveing events and preventing paddles from going off screen
def down(event):
    global autox, autoy,cordx,cordy
    y = 10
    x=0
    if(cordy == 390):
        return
    cordy = cordy +10
    myCanvas.move(block1,x,y)

def up(event):
    global autox, autoy,cordx,cordy
    y = -10
    x=0
    if(cordy == 0):
        return
    cordy = cordy -10
    myCanvas.move(block1,x,y)

def Q(event):
    global cordxx,cordyy
    y = 10
    x=0
    if(cordyy == 390):
        return
    cordyy = cordyy +10
    myCanvas.move(block2,x,y)

def A(event):
    global cordxx,cordyy
    y = -10
    x=0
    if(cordyy == 0):
        return
    cordyy = cordyy -10
    myCanvas.move(block2,x,y)


def move():
    global autox, autoy,ballx,bally,cordy,cordx,cordxx,cordyy,score2track,score1track
    #basic ball movement
    myCanvas.move(ball,autox,autoy)
    ballx = ballx + autox
    bally = bally + autoy
    #creates a random number for the verticle speed
    rand = random.randrange(-8,8)
    #checking if it bounces off the paddle
    if ballx == cordx+20 and bally >= cordy and bally+20 <= cordy+110:
        autox = 5
        autoy = rand
    #checking if it bounces off paddle
    if ballx == 430 and bally >= cordyy and bally+20 <= cordyy+110:
        autox = -5
        autoy = rand
    #checking if a point is scored
    if ballx < 0:
        myCanvas.coords(ball, 240,240,260,260)
        ballx = 240
        bally = 240
        myCanvas.itemconfig(score1, text= score1track+1)
        score1track = score1track+1
        autoy = rand
    if ballx >500:
        myCanvas.coords(ball, 240,240,260,260)
        ballx = 240
        bally = 240
        myCanvas.itemconfig(score2, text= score2track+1)
        score2track = score2track+1
        autoy = rand
        
    #checking if ball hits top wall or bottom wall
    if bally < 0: 
        autoy = -1*(autoy)
    if bally > 480:
        autoy = -1*(autoy)
    
    #lets see some movement
    window.after(50,move)
    
    #checking for interaction with food
   
#binding our movement functions
move()
window.bind("q", Q)
window.bind("a", A)
window.bind("<Down>",down)
window.bind("<Up>",up)

window.mainloop()