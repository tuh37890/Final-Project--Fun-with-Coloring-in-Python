#tiger,###fish,panda,###flamingo,###penguin

import turtle
t=turtle.Turtle()

##Tiger

import turtle
t = turtle.Turtle()

def tigerbody():
    t.speed(10)
    t.penup()
    t.pencolor("orange3")
    t.begin_fill()
    t.fillcolor("orange3")
    t.setpos(-60, -17)
    t.end_fill()
    t.penup()
    t.shape('turtle')
    t.shapesize(12,9,5)
    t.right(90)
    t.penup()

def tigerhead():
    import turtle
    t = turtle.Turtle()
    #body
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.pencolor("orange3")
    t.fillcolor("orange3")
    t.penup()
    t.goto(50,33)
    t.pendown
    t.circle(50)
    t.end_fill()

##face#####

def tigerlefteye():
    import turtle
    t = turtle.Turtle()
    t.penup()
    t.begin_fill()
    t.pencolor("white")
    t.fillcolor("white")
    t.penup()
    t.setpos(39, 95)
    t.pendown()
    t.circle(10)
    t.end_fill()
    t.hideturtle()

def tigerrighteye():
    import turtle
    t = turtle.Turtle()
    t.penup()
    t.begin_fill()
    t.pencolor("white")
    t.fillcolor("white")
    t.penup()
    t.setpos(65, 92)
    t.pendown()
    t.circle(10)
    t.end_fill()
    t.hideturtle()

def tigerleftinnereye():
    import turtle
    t = turtle.Turtle()
    t.penup()
    t.begin_fill()
    t.pencolor("black")
    t.fillcolor("black")
    t.penup()
    t.setpos(39, 95)
    t.pendown()
    t.circle(3)
    t.end_fill()
    t.hideturtle()


def tigerrightinnereye():
    import turtle
    t = turtle.Turtle()
    t.penup()
    t.begin_fill()
    t.pencolor("black")
    t.fillcolor("black")
    t.penup()
    t.setpos(65, 92)
    t.pendown()
    t.circle(3)
    t.end_fill()
    t.hideturtle()


def tigerDrawface():
    import turtle
    t = turtle.Turtle()
    t.penup()
    t.setpos(55, 55)
    t.pendown()
    t.right(90)
    t.circle(5, 180)
    t.penup()
    t.setpos(55, 55)
    t.pendown()
    t.left(360)
    t.circle(5, -180)
    t.hideturtle()

def tigerleftear():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.setpos(10, 125)
    t.pendown()
    t.pencolor("orange3")
    t.fillcolor("orange3")
    t.shape('triangle')
    t.right(45)
    t.shapesize(2)
    t.end_fill()

def tigerleftinnerear():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.setpos(10, 125)
    t.pendown()
    t.pencolor("pink")
    t.fillcolor("pink")
    t.shape('triangle')
    t.right(45)
    t.shapesize(1)
    t.end_fill()



def tigerrightear():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.setpos(89, 125)
    t.pendown()
    t.pencolor("orange3")
    t.fillcolor("orange3")
    t.shape('triangle')
    t.right(45)
    t.shapesize(2)
    t.end_fill()


def tigerrightinnerear():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.setpos(89, 125)
    t.pendown()
    t.pencolor("pink")
    t.fillcolor("pink")
    t.shape('triangle')
    t.right(45)
    t.shapesize(1)
    t.end_fill()



def tigertail():
    import turtle
    t=turtle.Turtle()
    t.pensize(13)
    t.color("orange3")
    t.penup()
    t.setpos(-190,150)
    t.pendown()
    t.backward(30)
    t.forward(30)
    t.circle(-65,75)
    t.circle(-50,90)
    t.circle(65,75)
    t.circle(50,90)
    t.penup()
    t.pendown()
    t.begin_fill()
    t.fillcolor("orange3")
    t.end_fill()

def tigerleftfeet():
    import turtle
    t=turtle.Turtle()
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.setpos(-135, -89)
    t.pendown()
    t.pencolor("orange3")
    t.fillcolor("orange3")
    t.shape('square')
    t.right(45)
    t.shapesize(3)
    t.end_fill()

def tigerrightfeet():
    import turtle
    t=turtle.Turtle()
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.setpos(37, -80)
    t.pendown()
    t.pencolor("orange3")
    t.fillcolor("orange3")
    t.shape('square')
    t.right(45)
    t.shapesize(3)
    t.end_fill()

def tigerStripes():
    import turtle
    t=turtle.Turtle()
    #t.pensize(2)
    t.begin_fill()
    t.color("black")
    t.penup()
    t.setpos(-136,50)
    t.pendown()
    t.shape("triangle")
    t.shapesize(2)
    t.forward(115)
    t.penup()
    t.setpos(-163,20)
    t.pendown()
    t.forward(100)
    t.penup()
    t.setpos(-173,-40)
    t.pendown()
    t.forward(100)
    t.penup()
    t.setpos(-133,-90)
    t.pendown()
    t.forward(100)
    t.right(-220)
    t.forward(20)
    t.end_fill()

def moretigerstripes():
    import turtle
    t=turtle.Turtle()
    t.pensize(2)
    t.begin_fill()
    t.fillcolor("black")
    t.penup()
    t.setpos(26,50)
    t.right(120)
    t.pendown()
    t.forward(20)
    t.right(230)
    t.forward(25)
    t.end_fill()


############# PANDA BEAR ###########
###https://www.geeksforgeeks.org/draw-panda-using-turtle-graphics-in-python/ (citation for the head only/rest was coded by me)
### Draw a Panda using Turtle Graphics
### Import turtle package
##import turtle
##
### Creating a turtle object(pen)
##pen = turtle.Turtle()
##
### Defining method to draw a colored circle
### with a dynamic radius
##def ring(col, rad):
##
##	# Set the fill
##	pen.fillcolor(col)
##
##	# Start filling the color
##	pen.begin_fill()
##
##	# Draw a circle
##	pen.circle(rad)
##
##	# Ending the filling of the color
##	pen.end_fill()
##
##
### Draw first ear
##import turtle
##pen = turtle.Turtle()
##pen.up()
##pen.setpos(-35, 95)
##pen.down
##ring('black', 15)
##
### Draw second ear
##pen.up()
##pen.setpos(35, 95)
##pen.down()
##ring('black', 15)
##
####### Draw face #####
##pen.up()
##pen.setpos(0, 35)
##pen.down()
##ring('white', 40)
##
####### Draw eyes black #####
##
### Draw first eye
##pen.up()
##pen.setpos(-18, 75)
##pen.down
##ring('black', 8)
##
### Draw second eye
##pen.up()
##pen.setpos(18, 75)
##pen.down()
##ring('black', 8)
##
####### Draw eyes white #####
##
### Draw first eye
##pen.up()
##pen.setpos(-18, 77)
##pen.down()
##ring('white', 4)
##
### Draw second eye
##pen.up()
##pen.setpos(18, 77)
##pen.down()
##ring('white', 4)
##
####### Draw nose #####
##pen.up()
##pen.setpos(0, 55)
##pen.down
##ring('black', 5)
##
####### Draw mouth #####
##pen.up()
##pen.setpos(0, 55)
##pen.down()
##pen.right(90)
##pen.circle(5, 180)
##pen.up()
##pen.setpos(0, 55)
##pen.down()
##pen.left(360)
##pen.circle(5, -180)
##pen.hideturtle()
##
######Draw blackbody####
##pen.up()
##pen.setpos(-60, -17)
##pen.down()
##pen.right(90)
##pen.circle(5,80)
##ring('black',70)
##pen.up()
##pen.setpos(0, 55)
##
##
######Draw whitebody#####
##pen.up()
##pen.setpos(-30, -12)
##pen.down()
##pen.right(90)
##pen.circle(5,80)
##ring('white',40)
##pen.up()
##pen.setpos(0, 55)
##
##
##
######Draw Leftarm#####
##pen.up()
##pen.setpos(-78, 17)
##pen.down
##ring('black', 22)
##
##
######Draw rightarm#####
##pen.up()
##pen.setpos(55, 19)
##pen.down()
##ring('black', 22)
##
######Draw leftfoot####
##
##pen.up()
##pen.setpos(-78, -78)
##pen.down
##ring('black', 22)
##
######Draw righfoot####
##pen.up()
##pen.setpos(55, -78)
##pen.down()
##ring('black', 22)
##
######paws####
###leftpaw
##

#Fish

import turtle
t=turtle.Turtle()

def Draw_Fish(i,j):
    import turtle
    t=turtle.Turtle()
    sc = turtle.Screen()
    sc._color('orange')
    sc.bgcolor("#85C1E9")
    t.penup()
    t.goto(i,j)
    t.begin_fill()
    t.fillcolor("orange")
    t.speed(10)
    t.left(45)
    t.pendown()
    t.forward(100)
    t.right(135)
    t.forward(130)
    t.right(130)
    t.forward(90)
    t.left(90)
    t.right(90)
    t.circle(200,90)
    t.left(90)
    t.circle(200,90)
    t.penup()
    t.left(130)
    t.forward(200)
    t.pendown()
    t.circle(10,360)
    t.right(270)
    t.penup()
    t.forward(50)
    t.pendown()
    t.left(90)
    t.circle(100,45)
    t.penup()
    t.left(135)
    t.pendown()
    t.right(180)
    t.hideturtle()
    t.end_fill()
    t.hideturtle()
    
 
#Draw_Fish(0,0)



##    
###PENGUIN####
def penguinbodyblack():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.setpos(-60, -17)
    t.pendown()
    t.circle(50)
    t.end_fill()
    t.setpos(-60, -117)
    t.penup()
    t.shape('circle')
    t.shapesize(10,8,5)
    t.penup()
    

def penginnerbodyblack():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.setpos(-60, -17)
    t.pendown()
    t.circle(50)
    t.end_fill()
    t.setpos(-60, -117)
    t.penup()
    t.fillcolor("wheat")
    t.shape('circle')
    t.shapesize(7,6,5)
    t.penup()
    
#arms
#left arm
def pengleftarm():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.setpos(-140, -85)
    t.pendown()
    t.fillcolor("black")
    t.shape('circle')
    t.right(45)
    t.shapesize(6,1,1)
    t.end_fill()
    

#rightarm

def pengrightarm():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.setpos(30, -85)
    t.pendown()
    t.fillcolor("black")
    t.shape('circle')
    t.right(128)
    t.shapesize(6,1,1)
    t.end_fill()
    

#leftfeet
#import turtle
def pengleftfeet():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.setpos(-135, -200)
    t.pendown()
    t.fillcolor("orange")
    t.shape('circle')
    t.right(45)
    t.shapesize(3)
    t.end_fill()
    

#rightfeet
#import turtle
def pengrightfeet():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.setpos(10, -200)
    t.pendown()
    t.fillcolor("orange")
    t.shape('circle')
    t.right(128)
    t.shapesize(3)
    t.end_fill()
    


##
#####Beak-(Basically a diamond and a triangle)
def pengbeak():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.setpos(-60,30)
    t.pendown()
    t.fillcolor("orange")
    t.shape('triangle')
    t.shapesize(1)
    t.right(313)
    t.stamp()
    t.end_fill()
    
#eyes 

### Draw first eye

import turtle
def pengfirsteye():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.begin_fill()
    t.penup()
    t.setpos(-80, 50)
    t.pendown()
    t.fillcolor("white")
    t.circle(8)
    t.end_fill()
    t.hideturtle()

# Draw second eye
def pengsecondeye():
    import turtle
    t=turtle.Turtle()
    t.begin_fill()
    t.penup()
    t.setpos(-35, 50)
    t.pendown()
    t.fillcolor("white")
    t.circle(8)
    t.end_fill()
    t.hideturtle
  

####### Draw eyes white #####

## Draw first eye
def penginnereye1():
    import turtle
    t=turtle.Turtle()
    t.begin_fill()
    t.penup()
    t.setpos(-80, 50)
    t.pendown()
    t.fillcolor("DeepPink")
    t.circle(4)
    t.end_fill()
    t.hideturtle()

## Draw second eye
def penginnereye2():
    import turtle
    t=turtle.Turtle()
    t.begin_fill()
    t.penup()
    t.setpos(-35, 49)
    t.pendown()
    t.fillcolor("DeepPink")
    t.circle(4)
    t.end_fill()
    t.hideturtle()

#hair1
def penghair1():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.setpos(-60, 89)
    t.pendown()
    t.fillcolor("black")
    t.shape('arrow')
    t.shapesize(2)
    t.right(313)
    t.right(90)
    t.stamp()
    t.end_fill()
    

#hair2
def penghair2():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.setpos(-60, 89)
    t.pendown()
    t.fillcolor("black")
    t.shape('arrow')
    t.shapesize(1)
    t.right(313)
    t.right(45)
    t.stamp()
    t.end_fill()
   



##
###Flamingo
###body


def flambody():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.pencolor("pink")
    t.begin_fill()
    t.fillcolor("pink")
    t.setpos(-60, -17)
    t.end_fill()
    t.penup()
    t.shape('circle')
    t.shapesize(6,4,3)
    t.right(90)
    t.penup()



#neck
def flamneck():
    import turtle
    t=turtle.Turtle()
    t.pensize(13)
    t.color("pink")
    t.penup()
    t.setpos(-125,180)
    t.pendown()
    t.backward(30)
    t.forward(30)
    t.circle(-65,75)
    t.circle(-50,90)
    t.circle(65,75)
    t.circle(50,90)
    t.penup()
    t.setpos(-145,180)
    t.right(180)
    t.pendown()
    t.begin_fill()
    t.fillcolor("pink")
    t.circle(5)
    t.forward(10)
    t.circle(8)
    t.forward(10)
    t.left(45)
    t.circle(8)
    t.forward(10)
    t.circle(8)
    t.end_fill()



def flambeak():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.penup()
    t.begin_fill()
    t.setpos(-174,154)
    t.right(45)
    t.pendown()
    t.pencolor("black")
    t.fillcolor("black")
    t.shape('triangle')
    t.shapesize(1)
    t.right(313)
    t.stamp()
    t.end_fill()

def flamotherbeak():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.begin_fill()
    t.penup()
    t.goto(-174,154)
    t.pendown()
    t.pencolor("black")
    t.fillcolor("black")
    t.shape("circle")
    t.shapesize(1)
    t.right(313)
    t.forward(10)
    t.shape("circle")



def flameye():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.begin_fill()
    t.penup()
    t.setpos(-160, 175)
    t.pendown()
    t.pencolor("white")
    t.fillcolor("white")
    t.circle(4)
    t.end_fill()
    t.hideturtle()


def flamlegs():
    import turtle
    t=turtle.Turtle()
    t.speed(10)
    t.pensize(5)
    t.pencolor("black")
    t.fillcolor("black")
    t.penup()
    t.goto(-96,-45)
    t.pendown()
    t.right(-300)
    t.forward(100)
    t.circle(1)
    t.right(120)
    t.forward(50)
    t.circle(2)
    t.penup()
    t.goto(-68,-45)
    t.right(270)
    t.pendown()
    t.forward(140)
    t.circle(2)




animal='a'

    
while animal != 'exit':
    print("The zoo animals that we have are a panda,tiger,flamingo,penguin,fish, or enter exit")
    animal=input("Pick a zoo animal that you want to draw")
    if animal == 'panda':
            #ring('black', 22)
            continue
    elif animal == 'tiger':
            tigerbody()
            tigerhead()
            tigerlefteye()
            tigerrighteye()
            tigerleftinnereye()
            tigerrightinnereye()
            tigerDrawface()
            tigerleftear()
            tigerleftinnerear()
            tigerrightear()
            tigerrightinnerear()
            tigertail()
            tigerleftfeet()
            tigerrightfeet()
            tigerStripes()
            moretigerstripes()
    elif animal == 'flamingo':
            flambody()
            flamneck()
            flambeak()
            flamotherbeak()
            flameye()
            flamlegs()
        
    elif animal=='penguin':
            penguinbodyblack()
            penginnerbodyblack()
            pengleftarm()
            pengrightarm()
            pengleftfeet()
            pengrightfeet()
            pengbeak()
            pengfirsteye()
            pengsecondeye()
            penginnereye1()
            penginnereye2()
            penghair1()
            penghair2()
            
    elif animal =='fish':
            Draw_Fish(0,0)
    elif animal=='exit':
        break

    else:
        print("Invalid Input, enter the correct animal name")



##
##
##
##



