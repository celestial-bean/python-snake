highScore=3
try:
    import turtle
except importError:
    os.sys("pip install turtle")
import time
import random

alive=True
segments=[]

def die():
    alive = False
    playerScore=0   
    deathMessage.write("YOU DIED", align="center", font=("arial", 24, "normal"))
    time.sleep(3)
    exit()
def rand():
    return random.randint(-300, 300)
def up():
    if snake.direction != "down":
        snake.direction="up"

def right():
    if snake.direction != "left":
        snake.direction = "right"
def left():
    if snake.direction != "right":
        snake.direction="left"
def down():
    if snake.direction != "up":
        snake.direction ="down"
def move():
    
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(),segments[i-1].ycor())
        
    if len(segments) > 0:
        added_segment.showturtle()
        segments[0].goto(snake.xcor(), snake.ycor())
    if snake.direction =="up":
        snake.sety(snake.ycor()+20)
    if snake.direction =="right":
        snake.setx(snake.xcor()+20)
    if snake.direction== "left":
        snake.setx(snake.xcor()-20)
    if snake.direction == "down":
        snake.sety(snake.ycor()-20)
    
playerScore=0

delayTime=0.1

wind=turtle.Screen()
wind.bgcolor("grey")
wind.title("snake")

wind.setup(width=600, height=600)

snake=turtle.Turtle()
snake.shape("circle")
snake.color("green")
snake.penup()
snake.direction = "Stop"

food=turtle.Turtle()
food.color("red")
food.direction = "Stop"
food.penup()
food.speed(0)
food.shape("circle")

deathMessage=turtle.Turtle()
deathMessage.color("red")
deathMessage.penup()
deathMessage.hideturtle()

food.goto(rand(), rand())
snake.goto(rand(),rand())


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Player Score: 0 High Score: {}".format(highScore), align="center", font=("Arial", 24, "normal"))
    

wind.onkeypress(up, "w")
wind.onkeypress(down, "s")
wind.onkeypress(left, "a")
wind.onkeypress(right, "d")
wind.listen()
while alive:
    
 
    wind.update()
    move()
    
    if snake.xcor()>290 or snake.xcor() < -290 or snake.ycor() >290 or snake.ycor() < -290:
        die()
    if snake.distance(food)<20:
        playerScore+=1
        
        if playerScore>highScore:
            highScore=playerScore
            with open("snake.pyw", "r") as f:
                lines= f.read().split("\n")
            newLine= "highScore={}".format(highScore)
            with open("snake.pyw", "w") as f:
                f.write("\n".join([newLine] + lines[1:]))
                
        pen.clear()
        pen.write("Player Score: {} High Score: {}".format(playerScore, highScore), align="center", font=("Arial", 24, "normal"))
      
        food.goto(rand(), rand())
        delayTime/=1.1
        
        added_segment=turtle.Turtle()
        added_segment.hideturtle()
        added_segment.penup()
        added_segment.shape("circle")
        added_segment.speed(0)
        added_segment.color("white")
        segments.append(added_segment)
        
    time.sleep(delayTime)
    
    for i in segments:
        if i.distance(snake)<20:
            die()
            

turtle.mainloop()




