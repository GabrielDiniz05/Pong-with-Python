import turtle


gs = turtle.Screen()
gs.title("Pong in Python")
gs.bgcolor("black")
gs.setup(width=800, height=600)
gs.tracer(0)


# Player1
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("white")
p1.shapesize(stretch_wid=5, stretch_len=1)
p1.penup()
p1.goto(-350, 0)


# Player2
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("white")
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.penup()
p2.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.07
ball.dy = -0.07


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player1: 0  Player2: 0", align="center", font=("Courier", 24, "normal"))


# Score
score_1 = 0
score_2 = 0


# Function
def player1_up():
    y = p1.ycor()
    y += 20
    p1.sety(y)

def player1_down():
    y = p1.ycor()
    y -= 20
    p1.sety(y)

def player2_up():
    y = p2.ycor()
    y += 20
    p2.sety(y)

def player2_down():
    y = p2.ycor()
    y -= 20
    p2.sety(y)


# Keyboard binding
gs.listen()

gs.onkeypress(player1_up, "w")
gs.onkeypress(player1_down, "s")

gs.onkeypress(player2_up, "Up")
gs.onkeypress(player2_down, "Down")
        

def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


def player_ball_collision():
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < p2.ycor() + 40 and ball.ycor() > p2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < p1.ycor() + 40 and ball.ycor() > p1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1


while True:
    gs.update()

    move_ball()

    player_ball_collision()

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write(f"Player1: {score_1}  Player2: {score_2}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write(f"Player1: {score_1}  Player2: {score_2}", align="center", font=("Courier", 24, "normal"))