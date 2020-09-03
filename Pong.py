#Pong :)

import turtle

# Instance variables
window = True
game = True
# Window setup
win = turtle.Screen()
win.title=("Pong :)")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)


# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# Score
scoreA = 0
scoreB = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
#pen.write("Player A: " + str(scoreA) + " Player B : " + str(scoreB), align="center", font=("Courier", 24, "normal")) 
# Function
def paddleAUp():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleADown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddleBUp():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleBDown():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

#resets whole game
def reset():
    pen.goto(0,260)
    paddleA.goto(-350, 0)
    paddleB.goto(350, 0)
    scoreA = 0
    scoreB = 0
    game = True

# Update Scoreboard
    pen.clear()
    pen.write("Player A: " + str(scoreA) + " Player B : " + str(scoreB), align="center", font=("Courier", 24, "normal")) 


# Keyboard Binding
win.listen()
win.onkeypress(paddleAUp, "w")
win.onkeypress(paddleADown, "s")

win.onkeypress(paddleBUp, "Up")
win.onkeypress(paddleBDown, "Down")

win.onkeypress(reset, "y")


# Main game loops
while window:
    win.update()
    if game:
        # Move ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if (ball.ycor() > 290):
            ball.sety(290)
            ball.dy *= -1

        if (ball.ycor() < -290):
            ball.sety(-290)
            ball.dy *= -1

        if (ball.xcor() > 390):
            ball.goto(0, 0)
            ball.dx *= -1
            scoreA += 1

        if (ball.xcor() < -390):
            ball.goto(0, 0)
            ball.dx *= -1
            scoreB += 1
        
        if(paddleA.ycor() > 250):
            paddleA.sety(250)

        if(paddleB.ycor() > 250):
            paddleB.sety(250)
        
        if(paddleA.ycor() < -250):
            paddleA.sety(-250)

        if(paddleB.ycor() < -250):
            paddleB.sety(-250)


        
        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB. ycor() - 50):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA. ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1

        # Update Scoreboard
        pen.clear()
        pen.write("Player A: " + str(scoreA) + " Player B : " + str(scoreB), align="center", font=("Courier", 24, "normal")) 

        # End game if score goes over 8
        if scoreA == 8 or scoreB == 8:
            game = False
        
        if (scoreA == 8):
            pen.clear()
            pen.goto(0,200)
            pen.write("Player A Won!", align="center", font=("Courier", 24, "normal"))

        elif(scoreB == 8):
            pen.clear(0,200)
            pen.write("Player B Won!", aligssn="center", font=("Courier", 24, "normal"))


    



