# Pong
Simple pong game

execution steps
1. install both python and the tkinter libary
2. excute the file

General explanation
-------------------
The program works by first defining a canvas, the scores, the paddles and the ball.
Afterwards i defined the movement in both paddles, making them be able to go up and down. (I limited there movement to the page, meaning they cant go past the upper or lower border of the of the screen)
This left the balls movement, the ball constinitally moves so this required me to constanly excute the code, to do this i called the function in itself. 
This left only to determine when the ball needs to bounce, i saved the upper and lower edge of the ball and checked if its location ever reached the paddle or walls. 
If the the ball hits the paddle or the bottum/top of the screen it will reverse the movement of the balls y-cordinate.
If the ball hits the left or right wall it adds a point to the side it hits. the ball is then sent back to the middle of the screen with the same velocity. 
