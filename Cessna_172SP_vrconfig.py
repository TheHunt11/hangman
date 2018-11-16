# this is my awesome (non-violent) hang person game

from turtle import *
from random import randint
import time
import math

wordlist = ['zenith', 'zealot', 'yearn', 'yawner', 'xenophobia', 'x-axis', \
'wonky', 'wanton', 'vermillion', 'vague', 'unique', 'uncanny', 'tenacious',\
'tangible', 'serene', 'saquinavir', 'rhetorical', 'rambunctious', 'quixotic', 'quell']

sw = 500
sh = 500
s=getscreen()
s.setup(750, 400)
s.bgcolor('#42f4eb')
t1=getturtle()
t1.speed(0)

#we need to make another turtle
tWriter = Turtle()
tWriter.hideturtle()
#twriter.shape('turtle')

#Lets Make One for Wrong Letters, too 
tBadLetters = Turtle()
tBadLetters.hideturtle()

#variables to play the game
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettersWrong ="" #starting as empty strings
lettersCorrect = ""
secretWord =""
displayWord =""
fails = 6 #how many wrong guesses you have
fontS = int(sh*0.04)
gameDone = False

def getGuess():
  #boxTitle="Letters Used: " + lettersWrong
  #guess = s.textinput(boxTitle, "Enter a guess type $$ to guess the word")
  theGuess = input("Enter a guess type $$ to guess the word")
  return theGuess
  
def updateHangman():
  global fails
  if fails == 5:
    drawHead()
    #drawFace()
  if fails == 4:
    drawTorso()
  if fails == 3:
    drawRLeg()
  if fails == 2:
    drawLLeg()
  if fails == 1:
    drawRArm()
  if fails == 0:
    drawLArm()
      

def checkWordGuess():
  global fails, gameDone, alpha, lettersCorrect, lettersWrong
  boxTitle="Word Guess"
  theGuess = input ("Ok Awesome...Guess the word" )
  if theGuess == secretWord:
    displayText("YES! The word is " + secretWord)
    gameDone = True
  else:
    displayText("No the word is not " + theGuess)
    time.sleep(1)
    displayText(displayWord)
    fails -=1
    updateHangman()

def playGame():
  global gameDone, fails, lettersCorrect, lettersWrong
  print(gameDone)
  print(fails)
  while gameDone == False and fails > 0:
    # get input
    print("in main loop")
    theGuess = getGuess()
    #gameDone = True
    if theGuess == "$$":
      print("Let them guess word")
      checkWordGuess()
    elif len(theGuess) > 1 or theGuess =="":
        displayText("Sorry i need a letter, guess again")
        time.sleep(1)
        displayText(displayWord)
        print(gameDone)
        print(fails)
    elif theGuess not in alpha:
      displayText(theGuess + " is not a letter, guess again.")
      time.sleep(1)
      displayText(displayWord)
    elif theGuess.lower() in secretWord.lower():
      lettersCorrect += theGuess.lower()
      makeWordString()
      displayText(displayWord)
    else:
      if theGuess not in lettersWrong:
        lettersWrong += theGuess.lower()
        fails -= 1
        displayText(theGuess +" is not in the word")
        time.sleep(1)
        updateHangman()
        displayText(displayWord)
        displayBadLetters ("Not in word: [" + lettersWrong + "]")
      else:
        displayText(theGuess + " was already guessed. Try again")
        time.sleep(1)
        displayText(displayWord)
  #end of loop tests
    if "_" not in displayWord:
      display("Yes! You got it, the word is: " + secretWord)
    if fails <= 0:
      displayText("Sorry out of guesses-Word is: " + secretWord)
      gameDone = True

def chooseSecretWord():
  global secretWord
  secretWord = wordlist[randint(0, len(wordlist)-1 )]
  print("The secret word is " + secretWord)

def displayText(newText):
  tWriter.clear()
  tWriter.penup()
  tWriter.goto(-int(sw*0.7), -int(sh*0.3) )
  tWriter.write( newText, font=("Arial", fontS , "Bold") )
  
def displayBadLetters(newText):
  tBadLetters.clear()
  tBadLetters.penup()
  tBadLetters.goto(-int(sw*0.7), int(sh*0.3) )
  tBadLetters.write(newText, font=("Arial", fontS , "Bold") )
  
def makeWordString():
  global displayWord, alpha
  displayWord = ""
  for l in secretWord:
    if str(l) in alpha:
      if str(l).lower() in lettersCorrect.lower():
        displayWord += str(l) + " "
      else:
        displayWord += "_" + " "
    else:
     displayWord += str(l) + " "
  print(displayWord)

def drawGallows():
  t1.width(5)
  t1.color('black')
  t1.penup()
  t1.setheading(0)
  t1.goto(-int(sw/4), -int(sh/4) )
  t1.pendown()
  t1.forward(int(sw*0.3))
  t1.left(90)
  t1.forward(300)
  t1.left(90)
  t1.forward(150)
  t1.left(90)
  t1.forward(50)
  
def drawHead():
  hR = int(sw * 0.05)
  t1.penup()
  t1.goto(t1.xcor() - hR, t1.ycor()-hR)
  t1.pendown()
  t1.circle(hR)
  t1.penup()
  t1.goto(t1.xcor() + hR, t1.ycor()-hR)
  
  
def drawTorso():
  t1.pendown()
  t1.forward(30)
  
def drawRArm():
  x = t1.xcor()
  y = t1.ycor()
  h = t1.heading()
  t1.left(45)
  t1.forward(45)
  t1.goto(x, y)
  t1.setheading(h)
 
def drawLArm():
  x = t1.xcor()
  y = t1.ycor()
  h = t1.heading()
  t1.right(45)
  t1.forward(45)
  t1.goto(x, y)
  t1.setheading(h)
  
def drawBody():
  t1.forward(70)
  
def drawRLeg():
  x = t1.xcor()
  y = t1.ycor()
  h = t1.heading()
  t1.left(45)
  t1.forward(45)
  t1.goto(x, y)
  t1.setheading(h)
 
def drawLLeg():
  x = t1.xcor()
  y = t1.ycor()
  h = t1.heading()
  t1.right(45)
  t1.forward(45)
  t1.goto(x, y)
  t1.setheading(h)
  t1.penup
  

 
  
#game starts here
drawGallows()
drawHead()
drawTorso()
drawRArm()
drawLArm()
drawBody()
drawRLeg()
drawLLeg()

t1.clear()
chooseSecretWord()
drawGallows()
makeWordString()

time.sleep(1)

displayText("Guess a letter")
displayBadLetters("Not in word: [" + lettersWrong + "]")
time.sleep(1)
makeWordString()
displayText(displayWord)
playGame()
