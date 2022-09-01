import turtle 
screen=turtle.Screen()
screenTk=screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen",True)
t=turtle.Turtle()

t.penup()
t.goto(-500,200) #centering in the screen

#j
t.pendown()
t.pensize(20)
t.pencolor("blue")
t.forward(10)
t.right(90)
t.forward(150)
t.circle(-50,180)

#A
t.penup()
t.goto(-385,200) #centering in the screen

t.pendown()
 
t.right(160)
t.forward(200)
 
t.setpos(-385,200)
t.right(40)
t.forward(200)
 
t.penup()
t.setpos(-410,130)
t.right(65)
t.pendown()
t.backward(50)

#V
t.penup()
t.goto(-325,200) #centering in the screen
t.pendown()
t.right(255)
t.forward(200)
t.left(140)
t.forward(200)

#O
t.penup()
t.goto(18,75)

t.pendown()
t.pensize(20)
t.pencolor("red")
t.circle(90,None,75)

#N
t.penup()

t.goto(50,200) #centering in the screen
t.pendown()

t.right(158.5)
t.forward(200)
 
t.goto(50,200)
t.goto(180,0)
t.goto(180,200)

#A
t.penup()
t.goto(295,200) #centering in the screen

t.pendown()
 
t.right(18)
t.forward(200)
 
t.setpos(295,200)
t.right(-40)
t.forward(200)
 
t.penup()
t.setpos(270,130)
t.right(100)#-20
t.pendown()
t.backward(50)

#M
t.penup()
#draw straight line
t.goto(400,10) #centering in the screen
t.pendown()

#t.right(18)
#t.forward(150)
 
t.goto(400,200)
t.goto(460,150)
t.goto(520,200)
t.goto(520,10)



