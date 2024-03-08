################################################################################################################################################
#                       This is the board game layout and design section
################################################################################################################################################
score1= 0#The score variable values are set globally
score2= 0
import turtle
def main():
    import turtle
    turtle.title("Snakes and Ladders")#This changes the title of the tab to snakes and ladders
    turtle.setup(width=1300, height=900)#This makes the game screen larger when launched
    lines = turtle.Turtle()#imports new turtle: lines
    lines.ht()
    lines.speed(0)
    lines.penup()
    lines.pencolor("black")
    lines.pensize(7)
    lines.goto(-350,350)
    lines.pendown()
    turtle.bgcolor("#C1E0FF")
#The drawing of the square
    lines.goto(-350,-350)
    lines.goto(350,-350)
    lines.goto(350,350)
    lines.goto(-350,350)
#The drawing of the vertical lines
    lines.goto(-210,350)
    lines.goto(-210,-350)
    
    lines.goto(-70,-350)
    lines.goto(-70,350)
    
    lines.goto(70,350)
    lines.goto(70,-350)
    
    lines.goto(210,-350)
    lines.goto(210,350)
    
    lines.goto(350,350)
    lines.goto(350,350)
#The drawing of the horizontal lines
    lines.goto(350,210)
    lines.goto(-350,210)
    
    lines.goto(-350,70)
    lines.goto(350,70)
    
    lines.goto(350,-70)
    lines.goto(-350,-70)
    
    lines.goto(-350,-210)
    lines.goto(350,-210)
#The input of the numbers for each box
    numbers = turtle.Turtle()#imports new turtle: numbers
    numbers.ht()
    numbers.speed(0)
    numbers.penup()
    numbers.pencolor("black")
    numbers.pensize(7)
    numbers.goto(-350,350)
    numbers.pendown()
    
    numbers.penup()
    numbers.goto(-340,-250)
    numbers.pendown()
    numbers.write("1", font=("Verdana",
                                17, "normal"))#This one is number 1

    numbers.penup()
    numbers.goto(-200,-250)
    numbers.pendown()
    numbers.write("2", font=("Verdana",
                                17, "normal"))#this one is number 2

    numbers.penup()
    numbers.goto(-60,-250)
    numbers.pendown()
    numbers.write("3", font=("Verdana",
                                17, "normal"))#this one is number 3
    numbers.penup()
    numbers.goto(80,-250)
    numbers.pendown()
    numbers.write("4", font=("Verdana",
                                17, "normal"))#this one is number 4

    numbers.penup()
    numbers.goto(220,-250)
    numbers.pendown()
    numbers.write("5", font=("Verdana",
                                17, "normal"))#this one is number 5

    numbers.penup()
    numbers.goto(220,-110)
    numbers.pendown()
    numbers.write("6", font=("Verdana",
                                17, "normal"))#this one is number 6

    numbers.penup()
    numbers.goto(80,-110)
    numbers.pendown()
    numbers.write("7", font=("Verdana",
                                17, "normal"))#this one is number 7

    numbers.penup()
    numbers.goto(-60,-110)
    numbers.pendown()
    numbers.write("8", font=("Verdana",
                                17, "normal"))#this one is number 8

    numbers.penup()
    numbers.goto(-200,-110)
    numbers.pendown()
    numbers.write("9", font=("Verdana",
                                17, "normal"))#this one is number 9

    numbers.penup()
    numbers.goto(-340,-110)
    numbers.pendown()
    numbers.write("10", font=("Verdana",
                                17, "normal"))#this one is number 10

    numbers.penup()
    numbers.goto(-340,30)
    numbers.pendown()
    numbers.write("11", font=("Verdana",
                                17, "normal"))#this one is number 11

    numbers.penup()
    numbers.goto(-200,30)
    numbers.pendown()
    numbers.write("12", font=("Verdana",
                                17, "normal"))#this one is number 12

    numbers.penup()
    numbers.goto(-60,30)
    numbers.pendown()
    numbers.write("13", font=("Verdana",
                                17, "normal"))#this one is number 13

    numbers.penup()
    numbers.goto(80,30)
    numbers.pendown()
    numbers.write("14", font=("Verdana",
                                17, "normal"))#this one is number 14

    numbers.penup()
    numbers.goto(220,30)
    numbers.pendown()
    numbers.write("15", font=("Verdana",
                                17, "normal"))#this one is number 15

    numbers.penup()
    numbers.goto(220,170)
    numbers.pendown()
    numbers.write("16", font=("Verdana",
                                17, "normal"))#this one is number 16

    numbers.penup()
    numbers.goto(80,170)
    numbers.pendown()
    numbers.write("17", font=("Verdana",
                                17, "normal"))#this one is number 17

    numbers.penup()
    numbers.goto(-60,170)
    numbers.pendown()
    numbers.write("18", font=("Verdana",
                                17, "normal"))#this one is number 18

    numbers.penup()
    numbers.goto(-200,170)
    numbers.pendown()
    numbers.write("19", font=("Verdana",
                                17, "normal"))#this one is number 19

    numbers.penup()
    numbers.goto(-340,170)
    numbers.pendown()
    numbers.write("20", font=("Verdana",
                                17, "normal"))#this one is number 20

    numbers.penup()
    numbers.goto(-340,310)
    numbers.pendown()
    numbers.write("21", font=("Verdana",
                                17, "normal"))#this one is number 21

    numbers.penup()
    numbers.goto(-200,310)
    numbers.pendown()
    numbers.write("22", font=("Verdana",
                                17, "normal"))#this one is number 22

    numbers.penup()
    numbers.goto(-60,310)
    numbers.pendown()
    numbers.write("23", font=("Verdana",
                                17, "normal"))#this one is number 23

    numbers.penup()
    numbers.goto(80,310)
    numbers.pendown()
    numbers.write("24", font=("Verdana",
                                17, "normal"))#this one is number 24

    numbers.penup()
    numbers.goto(220,310)
    numbers.pendown()
    numbers.write("25", font=("Verdana",
                                17, "normal"))#this one is number 25
    

#This is the input for snake1(Orange snake)
    def snake():
        import turtle
        snake = turtle.Turtle()
        snakes = turtle.Screen()
        snakes.addshape("snake.gif")
        snake.shape("snake.gif")
        snake.penup()
        snake.goto(140,140)
    snake()
    #This is the input for snake2(Red snake)
    def snake2():
        import turtle
        snake2= turtle.Turtle()
        snakes2= turtle.Screen()
        snakes2.addshape("snake2.gif")
        snake2.shape("snake2.gif")
        snake2.penup()
        snake2.goto(0,-200)
    snake2()
    #This is the input for snake3(Pink snake)
    def snake3():
        import turtle
        snake3 = turtle.Turtle()
        snakes3 = turtle.Screen()
        snakes3.addshape("snake3.gif")
        snake3.shape("snake3.gif")
        snake3.penup()
        snake3.goto(-290,-70)
    snake3()
    #This is the input for ladder1(ladder between 9-12)
    def ladder():
        import turtle
        ladder = turtle.Turtle()
        ladders = turtle.Screen()
        ladders.addshape("ladder.gif")
        ladder.shape("ladder.gif")
        ladder.penup()
        ladder.goto(-120,-70)
    ladder()
    #This is the input for ladder2(ladder between 18-23)
    def ladder2():
        import turtle
        ladder2 = turtle.Turtle()
        ladders2 = turtle.Screen()
        ladders2.addshape("ladder2.gif")
        ladder2.shape("ladder2.gif")
        ladder2.penup()
        ladder2.goto(0,190)
    ladder2()
    #This is the input for ladder3(ladder between 5-15)
    def ladder3():
        import turtle
        ladder3 = turtle.Turtle()
        ladders3 = turtle.Screen()
        ladders3.addshape("ladder3.gif")
        ladder3.shape("ladder3.gif")
        ladder3.penup()
        ladder3.goto(280,-140)
    ladder3()  
################################################################################################################################################
#                       This is the character movement/ dice roll section
################################################################################################################################################

    print("------------------------------")
    print("New game:")
    print("Enter a name for the Cow")
    name1= input()
    print("Enter a name for the Bull")
    name2= input()
    print("------------------------------")
#Score turtles are made to write the score on the screen for the user to see
    import turtle
    scoreboard1 = turtle.Turtle()
    scoreboard1.ht()
    scoreboard1.speed(0)
    scoreboard1.penup()
    scoreboard1.pencolor("black")
    scoreboard1.pensize(7)
    scoreboard1.goto(370,150)
    scoreboard1.pendown()

    scoreboard1.penup()
    scoreboard1.goto(370,150)
    scoreboard1.pendown()
    scoreboard1.write((name1,"score=",score1), font=("Verdana",
                                15, "normal"))
    
    import turtle
    scoreboard2 = turtle.Turtle()
    scoreboard2.ht()
    scoreboard2.speed(0)
    scoreboard2.penup()
    scoreboard2.pencolor("black")
    scoreboard2.pensize(7)
    scoreboard2.goto(370,100)
    scoreboard2.pendown()

    scoreboard2.penup()
    scoreboard2.goto(370,100)
    scoreboard2.pendown()
    scoreboard2.write((name2,"score=",score2), font=("Verdana",
                                15, "normal"))
    def characters():
    #A new turtle is imported: cow
        import turtle
        cow = turtle.Turtle()
        cow.speed(2)
        cow1 = turtle.Screen()
        cow1.addshape("cow.gif")
        cow.shape("cow.gif")
        cow.penup()
        cow.goto(-300,-320)

    #A new turtle is imported: bull
        import turtle
        bull = turtle.Turtle()
        bull.speed(2)
        bull2 = turtle.Screen()
        bull2.addshape("bull.gif")
        bull.shape("bull.gif")
        bull.penup()
        bull.goto(-300,-270)


    #The roll function is defined so that the dice will roll when the user presses enter.
        def roll():
            b = 1
            cp = 1
            bp = 1
            global score1
            global score2
    #A while loop is added so the users can keep rolling the dice.
            while b==1:
                print(name1,":press enter to roll the dice")
                input()
                import random
                x= random.randint(1,6)#x is the number you roll on the dice
                if x == 1:
                    ocp = cp
                    cp += 1#cp is cow position which shows the user where they are on the board
                    import turtle
                    dice1 = turtle.Turtle()#The dice image for dice1 is added and moved accordingly
                    dice1.ht()
                    dicescreen = turtle.Screen()
                    dicescreen.addshape("dice1.gif")
                    dice1.shape("dice1.gif")
                    dice1.penup()
                    dice1.speed(0)
                    dice1.goto(390,300)
                    dice1.st()
                elif x == 2:
                    ocp = cp #A new variable is created:ocp= old cow position, this keeps track of the previous position the cow was in
                    cp += 2
                    import turtle
                    dice2 = turtle.Turtle()#The dice image for dice2 is added and moved accordingly
                    dice2.ht()
                    dicescreen = turtle.Screen()
                    dicescreen.addshape("dice2.gif")
                    dice2.shape("dice2.gif")
                    dice2.penup()
                    dice2.speed(0)
                    dice2.goto(390,300)
                    dice2.st()
                elif x == 3:
                    ocp = cp
                    cp += 3
                    import turtle
                    dice3 = turtle.Turtle()#The dice image for dice3 is added and moved accordingly
                    dice3.ht()
                    dicescreen = turtle.Screen()
                    dicescreen.addshape("dice3.gif")
                    dice3.shape("dice3.gif")
                    dice3.penup()
                    dice3.speed(0)
                    dice3.goto(390,300)
                    dice3.st()
                elif x == 4:
                    ocp = cp
                    cp += 4
                    import turtle
                    dice4 = turtle.Turtle()#The dice image for dice4 is added and moved accordingly
                    dice4.ht()
                    dicescreen = turtle.Screen()
                    dicescreen.addshape("dice4.gif")
                    dice4.shape("dice4.gif")
                    dice4.penup()
                    dice4.speed(0)
                    dice4.goto(390,300)
                    dice4.st()
                elif x == 5:
                    ocp = cp
                    cp += 5
                    import turtle
                    dice5 = turtle.Turtle()#The dice image for dice5 is added and moved accordingly
                    dice5.ht()
                    dicescreen = turtle.Screen()
                    dicescreen.addshape("dice5.gif")
                    dice5.shape("dice5.gif")
                    dice5.penup()
                    dice5.speed(0)
                    dice5.goto(390,300)
                    dice5.st()
                elif x == 6:
                    ocp = cp
                    cp += 6
                    import turtle
                    dice6 = turtle.Turtle()#The dice image for dice6 is added and moved accordingly
                    dice6.ht()
                    dicescreen = turtle.Screen()
                    dicescreen.addshape("dice6.gif")
                    dice6.shape("dice6.gif")
                    dice6.penup()
                    dice6.speed(0)
                    dice6.goto(390,300)
                    dice6.st()
#These instructions are used to move the cow depending on the dice roll.
#Also, they makes sure the cow stays inside the lines and does not go out and follows the path.

                if cp== 1 and ocp>=1 and ocp<=1:
                    cow.goto(-300, -320)
                elif cp== 2 and ocp>=1 and ocp<=2:
                    cow.goto(-150, -320)
                elif cp== 3 and ocp>=1 and ocp<=3:
                    cow.goto(0, -320)
                elif cp== 4 and ocp>=1 and ocp<=4:
                    cow.goto(150, -320)
                elif cp== 5 and ocp>=1 and ocp<=5:
                    cow.goto(300, -320)
                    cow.goto(300, -20)
                    cp+= 10
                elif cp== 6 and ocp>=1 and ocp<=6:
                    cow.goto(300, -320)
                    cow.goto(300, -170)
                elif cp== 7 and ocp>=6 and ocp<=7:
                    cow.goto(150, -170)
                elif cp== 7 and ocp>=1 and ocp<=5:
                    cow.goto(300, -320)
                    cow.goto(300, -170)
                    cow.goto(150, -170)

                elif cp== 8 and ocp>=6 and ocp<=8:
                    cow.goto(0, -170)
                    cow.goto(0, -320)
                    cp-= 5
                elif cp== 8 and ocp>=2 and ocp<=5:
                    cow.goto(300, -320)
                    cow.goto(300, -170)
                    cow.goto(0, -170)
                    cow.goto(0, -320)
                    cp-= 5

                elif cp== 9 and ocp>=6 and ocp<=8:
                    cow.goto(-150, -170)
                    cow.goto(-150, -20)

                    cp+= 3
                elif cp== 9 and ocp>=9 and ocp<=9:
                    cow.goto(-150, -170)
                    cp+= 3
                    
                elif cp== 9 and ocp>=3 and ocp<=5:
                    cow.goto(300, -320)
                    cow.goto(300, -170)
                    cow.goto(-150, -170)
                    cow.goto(-150, -20)
                    cp+= 3
                    
                elif cp== 10 and ocp>=6 and ocp<=10:
                    cow.goto(-300, -170)
                elif cp== 10 and ocp>=4 and ocp<=5:
                    cow.goto(300, -320)
                    cow.goto(300, -170)
                    cow.goto(-300, -170)

                    
                elif cp== 11 and ocp>11 and ocp<=11:
                    cow.goto(-300, -170)
                    cow.goto(-300, -20)
                elif cp== 11 and ocp<=5:
                    cow.goto(300, -320)
                    cow.goto(300, -170)
                    cow.goto(-300, -170)
                    cow.goto(-300, -20)
                elif cp== 11 and ocp>=6 and ocp<=10:
                    cow.goto(-300, -170)
                    cow.goto(-300, -20)
                    
                elif cp== 12 and ocp>=11 and ocp<=11:
                    cow.goto(-150, -20)
                elif cp== 12 and ocp>=6 and ocp<=8:
                    cow.goto(-300, -170)
                    cow.goto(-300, -20)
                    cow.goto(-150, -20)
                elif cp== 12 and ocp>=9 and ocp<=9:
                    cow.goto(-150, -20)
                elif cp== 12 and ocp>=10 and ocp<=10:
                    cow.goto(-300, -20)
                    cow.goto(-150, -20)

                    
                elif cp== 13 and ocp>=11 and ocp<=13:
                    cow.goto(0, -20)
                elif cp== 13 and ocp>=7 and ocp<=10:
                    cow.goto(-300, -170)
                    cow.goto(-300, -20)
                    cow.goto(0, -20)

                    
                elif cp== 14 and ocp>=11 and ocp<=14:
                    cow.goto(150, -20)
                elif cp== 14 and ocp>= 8 and ocp<=10:
                    cow.goto(-300, -170)
                    cow.goto(-300, -20)
                    cow.goto(150, -20)
            
                    
                elif cp== 15 and ocp>=11 and ocp<=15:
                    cow.goto(300, -20)
                elif cp== 15 and ocp>= 9 and ocp<=10:
                    cow.goto(-300, -170)
                    cow.goto(-300, -20)
                    cow.goto(300, -20)


                    
                elif cp== 16 and ocp>=16 and ocp<=16:
                    cow.goto(300, -20)
                    cow.goto(300,130 )
                elif cp== 16 and ocp<= 10:
                    cow.goto(-300, -170)
                    cow.goto(-300, -20)
                    cow.goto(300, -20)
                    cow.goto(300,130 )
                elif cp== 16 and ocp>=11 and ocp<=15:
                    cow.goto(300, -20)
                    cow.goto(300,130 )


                    
                elif cp== 17 and ocp>=16 and ocp<=17:
                    cow.goto(150,130 )
                elif cp== 17 and ocp>= 11 and ocp<=15:
                    cow.goto(300, -20)
                    cow.goto(300,130 )
                    cow.goto(150,130 )

                    
                elif cp== 18 and ocp>=16 and ocp<=18:
                    cow.goto(0,130 )
                    cow.goto(0,280 )
                    cp+=5
                elif cp== 18 and ocp>= 12 and ocp<=15:
                    cow.goto(300, -20)
                    cow.goto(300,130 )
                    cow.goto(0,130 )
                    cow.goto(0,280 )
                    cp+=5


                elif cp== 19 and ocp>=16 and ocp<=19:
                    cow.goto(-150,130 )
                elif cp== 19 and ocp>= 13 and ocp<=15:
                    cow.goto(300, -20)
                    cow.goto(300,130 )
                    cow.goto(-150,130 )
                
                elif cp== 20 and ocp>=16 and ocp<=20:
                    cow.goto(-300,130 )
                    cow.goto(-300, -320)
                    cp-= 19
                elif cp== 20 and ocp>= 14 and ocp<=15:
                    cow.goto(300, -20)
                    cow.goto(300,130 )
                    cow.goto(-300,130 )
                    cow.goto(-300, -320)
                    cp-= 19


                elif cp== 21 and ocp>=16 and ocp<=20:
                    cow.goto(-300,130 )
                    cow.goto(-300,280 )
                elif cp== 21 and ocp>=15 and ocp<=15:
                    cow.goto(300, -20)
                    cow.goto(300,130)
                    cow.goto(-300,130 )
                    cow.goto(-300,280 )
     
                elif cp== 22 and ocp>=21 and ocp<=22:
                    cow.goto(-150,280 )
                elif cp== 22 and ocp>= 16 and ocp<=20:
                    cow.goto(-300,130 )
                    cow.goto(-300,280 )
                    cow.goto(-150,280 )

                             
                elif cp== 23 and ocp>=21 and ocp<=23:
                    cow.goto(0,280 )
                elif cp== 23 and ocp>= 17 and ocp<=20:
                    cow.goto(-300,130 )
                    cow.goto(-300,280 )
                    cow.goto(0,280 )

                             
                elif cp== 24 and ocp>=21 and ocp<=24:
                    cow.goto(150,280 )
                    cow.goto(150, -20)
                    cp-= 10
                elif cp== 24 and ocp>= 18 and ocp<=20:
                    cow.goto(-300,130 )
                    cow.goto(-300,280 )
                    cow.goto(150,280 )
                    cow.goto(150, -20)
                    cp-= 10

                    
                if cp>= 25 and ocp>=21 and ocp<=25:
                    cow.goto(300,280 )
                    if cp>= 25:#This gives a message to the user letting them know they have won.
                        print("Congradulations",name1, "you WON!!!")
                        import turtle
                        win = turtle.Turtle()
                        win.speed(0)
                        winnner = turtle.Screen()
                        winnner.addshape("win.gif")
                        win.shape("win.gif")
                        win.penup()
                        win.goto(0,0)

                    
                if cp>= 25 and ocp>= 19 and ocp<=20:
                    cow.goto(-300,130 )
                    cow.goto(-300,280 )
                    cow.goto(300,280 )
                    if cp>= 25:#This gives a message to the user letting them know they have won.
                        print("Congradulations",name1, "you WON!!!")
                        import turtle
                        win = turtle.Turtle()
                        win.speed(0)
                        winnner = turtle.Screen()
                        winnner.addshape("win.gif")
                        win.shape("win.gif")
                        win.penup()
                        win.goto(0,0)
                if cp>=25:
                        score1+=1#This command adds 1 to the score when the cow wins and prints it for the user to see the score
                        print(name1,"score is", score1)
                        answer = input('Play again? (y/n): ')#This is a reset function giving the user the option to restart or quit
                        if answer== "y":
                            turtle.reset()
                            turtle.ht()
                            win.ht()
                            scoreboard2.reset()#resets and upgrades the scoreboard
                            scoreboard1.reset()#resets and upgrades the scoreboard
                            scoreboard2.ht()
                            scoreboard1.ht()
                            main()
                        else:
                            turtle.bye()
                            break

                    
                print(name1,"moved",x, "steps forward")#Tells the user what they have rolled/moved
                print("you are at position", cp)#Tells the user the position they are in
                print("------------------------------")
                    
                print(name2,":press enter to roll the dice")
                input()
                import random
                x= random.randint(1,6)#x is the number you roll on the dice
                if x == 1:
                    obp = bp#A new variable is created:obp= old bull position, this keeps track of the previous position the bull was in
                    bp += 1#bp is bull position which shows the user where they are on the board
                    import turtle
                    dices1 = turtle.Turtle()#The dice image for dice1 is added and moved accordingly
                    dices1.ht()
                    dicescreen.addshape("dice1.gif")
                    dices1.shape("dice1.gif")
                    dices1.penup()
                    dices1.speed(0)
                    dices1.goto(390,300)
                    dices1.st()
                
                elif x == 2:
                    obp = bp
                    bp += 2
                    import turtle
                    dices2 = turtle.Turtle()#The dice image for dice2 is added and moved accordingly
                    dices2.ht()
                    dicescreen = turtle.Screen()
                    dicescreen.addshape("dice2.gif")
                    dices2.shape("dice2.gif")
                    dices2.penup()
                    dices2.speed(0)
                    dices2.goto(390,300)
                    dices2.st()
                elif x == 3:
                    obp = bp
                    bp += 3
                    import turtle
                    dices3 = turtle.Turtle()#The dice image for dice3 is added and moved accordingly
                    dices3.ht()
                    dicescreen = turtle.Screen()
                    dicescreen.addshape("dice3.gif")
                    dices3.shape("dice3.gif")
                    dices3.penup()
                    dices3.speed(0)
                    dices3.goto(390,300)
                    dices3.st()
                elif x == 4:
                    obp = bp
                    bp += 4
                    import turtle
                    dices4 = turtle.Turtle()#The dice image for dice4 is added and moved accordingly
                    dices4.ht()
                    dicescreen = turtle.Screen()
                    dicescreen.addshape("dice4.gif")
                    dices4.shape("dice4.gif")
                    dices4.penup()
                    dices4.speed(0)
                    dices4.goto(390,300)
                    dices4.st()
                elif x == 5:
                    obp = bp
                    bp += 5
                    import turtle
                    dices5 = turtle.Turtle()#The dice image for dice5 is added and moved accordingly
                    dices5.ht()
                    dicescreen = turtle.Screen()
                    dicescreen.addshape("dice5.gif")
                    dices5.shape("dice5.gif")
                    dices5.penup()
                    dices5.speed(0)
                    dices5.goto(390,300)
                    dices5.st()
                elif x == 6:
                    obp = bp
                    bp += 6
                    import turtle
                    dices6 = turtle.Turtle()#The dice image for dice6 is added and moved accordingly
                    dices6.ht()
                    dicescreen = turtle.Screen()
                    dicescreen.addshape("dice6.gif")
                    dices6.shape("dice6.gif")
                    dices6.speed(0)
                    dices6.penup()
                    dices6.goto(390,300)
                    dices6.st()

#These instructions are used to move the bull depending on the dice roll.
#Also, they makes sure the bull stays inside the lines and does not go out and it follows the path.
                    
                if bp== 1 and obp>=1 and obp<=1:
                    bull.goto(-300, -270)
                elif bp== 2 and obp>=1 and obp<=2:
                    bull.goto(-150, -270)
                elif bp== 3 and obp>=1 and obp<=3:
                    bull.goto(0, -270)
                elif bp== 4 and obp>=1 and obp<=4:
                    bull.goto(150, -270)
                elif bp== 5 and obp>=1 and obp<=5:
                    bull.goto(300, -270)
                    bull.goto(300, 30)
                    bp+= 10
                elif bp== 6 and obp>=1 and obp<=6:
                    bull.goto(300, -270)
                    bull.goto(300, -120)
                elif bp== 7 and obp>=6 and obp<=7:
                    bull.goto(150, -120)
                elif bp== 7 and obp>=1 and obp<=5:
                    bull.goto(300, -270)
                    bull.goto(300, -120)
                    bull.goto(150, -120)

                elif bp== 8 and obp>=6 and obp<=8:
                    bull.goto(0, -120)
                    bull.goto(0, -270)
                    bp-= 5
                elif bp== 8 and obp>=2 and obp<=5:
                    bull.goto(300, -270)
                    bull.goto(300, -120)
                    bull.goto(0, -120)
                    bull.goto(0, -270)
                    bp-= 5

                elif bp== 9 and obp>=6 and obp<=8:
                    bull.goto(-150, -120)
                    bull.goto(-150, 30)
                    bp+= 3
                elif bp== 9 and obp>=9 and obp<=9:
                    bull.goto(-150, -120)
                    bp+= 3
                    
                elif bp== 9 and obp>=3 and obp<=5:
                    bull.goto(300, -270)
                    bull.goto(300, -120)
                    bull.goto(-150, -120)
                    bull.goto(-150, 30)
                    bp+= 3
                    
                elif bp== 10 and obp>=6 and obp<=10:
                    bull.goto(-300, -120)
                elif bp== 10 and obp>=4 and obp<=5:
                    bull.goto(300, -270)
                    bull.goto(300, -120)
                    bull.goto(-300, -120)

                    
                elif bp== 11 and obp>11 and obp<=11:
                    bull.goto(-300, -120)
                    bull.goto(-300, 30)
                elif bp== 11 and obp<=5:
                    bull.goto(300, -270)
                    bull.goto(300, -120)
                    bull.goto(-300, -120)
                    bull.goto(-300, 30)
                elif bp== 11 and obp>=6 and obp<=10:
                    bull.goto(-300, -120)
                    bull.goto(-300, 30)
                    
                elif bp== 12 and obp>=11 and obp<=11:
                    bull.goto(-150, 30)
                elif bp== 12 and obp>=6 and obp<=8:
                    bull.goto(-300, -120)
                    bull.goto(-300, 30)
                    bull.goto(-150, 30)
                elif bp== 12 and obp>=9 and obp<=9:
                    bull.goto(-150, 30)
                elif bp== 12 and obp>=10 and obp<=10:
                    bull.goto(-300, 30)
                    bull.goto(-150, 30)

                    
                elif bp== 13 and obp>=11 and obp<=13:
                    bull.goto(0, 30)
                elif bp== 13 and obp>=7 and obp<=10:
                    bull.goto(-300, -120)
                    bull.goto(-300, 30)
                    bull.goto(0, 30)

                    
                elif bp== 14 and obp>=11 and obp<=14:
                    bull.goto(150, 30)
                elif bp== 14 and obp>= 8 and obp<=10:
                    bull.goto(-300, -120)
                    bull.goto(-300, 30)
                    bull.goto(150, 30)
            
                    
                elif bp== 15 and obp>=11 and obp<=15:
                    bull.goto(300, 30)
                elif bp== 15 and obp>= 9 and obp<=10:
                    bull.goto(-300, -120)
                    bull.goto(-300, 30)
                    bull.goto(300, 30)


                    
                elif bp== 16 and obp>=16 and obp<=16:
                    bull.goto(300, 30)
                    bull.goto(300,180 )
                elif bp== 16 and obp<= 10:
                    bull.goto(-300, -120)
                    bull.goto(-300, 30)
                    bull.goto(300, 30)
                    bull.goto(300,180 )
                elif bp== 16 and obp>=11 and obp<=15:
                    bull.goto(300, 30)
                    bull.goto(300,180 )


                    
                elif bp== 17 and obp>=16 and obp<=17:
                    bull.goto(150,180 )
                elif bp== 17 and obp>= 11 and obp<=15:
                    bull.goto(300, 30)
                    bull.goto(300,180 )
                    bull.goto(150,180 )

                    
                elif bp== 18 and obp>=16 and obp<=18:
                    bull.goto(0,180 )
                    bull.goto(0,330 )
                    bp+=5
                elif bp== 18 and obp>= 12 and obp<=15:
                    bull.goto(300, 30)
                    bull.goto(300,180 )
                    bull.goto(0,180 )
                    bull.goto(0,330 )
                    bp+=5


                elif bp== 19 and obp>=16 and obp<=19:
                    bull.goto(-150,180 )
                elif bp== 19 and obp>= 13 and obp<=15:
                    bull.goto(300, 30)
                    bull.goto(300,180 )
                    bull.goto(-150,130 )
                
                elif bp== 20 and obp>=16 and obp<=20:
                    bull.goto(-300,180 )
                    bull.goto(-300, -270)
                    bp-= 19
                elif bp== 20 and obp>= 14 and obp<=15:
                    bull.goto(300, 30)
                    bull.goto(300,180 )
                    bull.goto(-300,180 )
                    bull.goto(-300, -270)
                    bp-= 19


                elif bp== 21 and obp>=16 and obp<=20:
                    bull.goto(-300,180 )
                    bull.goto(-300,330 )
                elif bp== 21 and obp>=15 and obp<=15:
                    bull.goto(300, 30)
                    bull.goto(300,180)
                    bull.goto(-300,180 )
                    bull.goto(-300,330 )
     
                elif bp== 22 and obp>=21 and obp<=22:
                    bull.goto(-150,330 )
                elif bp== 22 and obp>= 16 and obp<=20:
                    bull.goto(-300,180 )
                    bull.goto(-300,330 )
                    bull.goto(-150,330 )

                             
                elif bp== 23 and obp>=21 and obp<=23:
                    bull.goto(0,330 )
                elif bp== 23 and obp>= 17 and obp<=20:
                    bull.goto(-300,180 )
                    bull.goto(-300,330 )
                    bull.goto(0,330 )

                             
                elif bp== 24 and obp>=21 and obp<=24:
                    bull.goto(150,330 )
                    bull.goto(150, 30)
                    bp-= 10
                    
                elif bp== 24 and obp>= 18 and obp<=20:
                    bull.goto(-300,180 )
                    bull.goto(-300,330 )
                    bull.goto(150,330 )
                    bull.goto(150, 30)
                    bp-= 10

                    
                elif bp>= 25 and obp>=21 and obp<=25:
                    bull.goto(300,330 )
                    if bp>= 25:#This gives a message to the user letting them know they have won.
                        print("Congradulations",name2, "you WON!!!")
                        import turtle
                        win = turtle.Turtle()
                        win.speed(0)
                        winner = turtle.Screen()
                        winner.addshape("win.gif")
                        win.shape("win.gif")
                        win.penup()
                        win.goto(0,0)

                    
                if bp>= 25 and obp>= 19 and obp<=20:
                    bull.goto(-300,180 )
                    bull.goto(-300,330 )
                    bull.goto(300,330 )
                    if bp>= 25:#This gives a message to the user letting them know they have won.
                        print("Congradulations",name2, "you WON!!!")
                        import turtle
                        win = turtle.Turtle()
                        win.speed(0)
                        winnner = turtle.Screen()
                        winnner.addshape("win.gif")
                        win.shape("win.gif")
                        win.penup()
                        win.goto(0,0)
                if bp>=25:
                        score2+=1#This command adds 1 to the score when the bull wins and prints it for the user to see the score
                        print(name2,"score is", score2)
                        answer = input('Play again? (y/n): ')#This is a reset function giving the user the option to restart or quit
                        if answer== "y":
                            turtle.reset()
                            turtle.ht()
                            scoreboard1.reset()#resets and upgrades the scoreboard
                            scoreboard2.reset()#resets and upgrades the scoreboard
                            scoreboard2.ht()
                            scoreboard1.ht()
                            win.ht()
                            main()
                        else:
                            turtle.bye()
                            break

                    
                
                print("You moved",x, "steps forward")#Tells the user what they have rolled/moved
                print("you are at position", bp)#Tells the user the position they are in
                print("-------------------------------")


                
                

                



                

        roll()
    characters()

main()
            

        
        
                    
