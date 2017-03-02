import simplegui
import random
import math
guess= 15 
secret_number= 95
n= 7
def input_guess(inp):
    global n 
    global guess
    guess = float(inp)
    print " Your guess was"+" "+ inp
    if (guess < secret_number):
        print "Higher laaaaaaa :)))"
        n= n-1
        print " You have" +" " + str(n) + " left."
    elif (guess > secret_number):
        print"Lower laaaaaaa :)))"
        n=n-1
        print " You have" +" " + str(n) + " left."
    else :
        print "U ARE RIGHT, RESPECT!"
        print "------------------------------------------------------------------------------------------------------"
    if(n==0):
        print" YOU SUCK NOOB!"
        print "------------------------------------------------------------------------------------------------------"
    
     
      
    
def New_game():
    input_guess
    global secret_number
    global n
    n= int(n)
    n=7
    secret_number=random.randrange(0, 100)
    print"Ready to play????"
    print "your range is from 0 to 100"
    print "You have " +str(n) + " guesses."
    print " "
    
def range100():
    global secret_number 
    secret_number=random.randrange(0, 100)
    New_game()
def range1000():
    global n 
    n=15
    global secret_number 
    secret_number=random.randrange(0, 1000)
    print "Ready to play????"
    print "your range is from 0 to 1000"
    print "You have " +str(n) + " guesses."
    print " "
        
print "                       Guess the number game!!!!!"

frame = simplegui.create_frame('Testing', 200, 200, 300)  
inp= frame.add_input('My label', input_guess, 50)
button1 = frame.add_button('range 0-100',range100,100)
button2 = frame.add_button('range 0-1000',range1000,100)
frame.start
