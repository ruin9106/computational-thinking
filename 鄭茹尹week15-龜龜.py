import turtle 
shelly = turtle.Turtle() 
shelly.shape("turtle") 
shelly.position() 
shelly.color("green", "red") 
shelly.pencolor("black") 
shelly.turtlesize(10,10,2)
shelly.resizemode("auto") 
shelly.turtlesize(5,5,3) 
shelly.forward(100)
shelly.left(90)
shelly.penup()
shelly.pendown()
shelly.hideturtle()
shelly.begin_fill()
shelly.fillcolor("orange")
shelly.circle(250) 
shelly.circle(250, 180, 30)
shelly.end_fill()
shelly.stamp()
shelly.write("Turtle Rock")