money = 50
wagerAmount = 0
updatedMoney = 0
moneyResult = "x"
gameActive = True
userName = input("Hello! Can you please tell me your first name?")

import time
import sys
time.sleep(1)

if userName == "Layne":
    print("Layne's are not ALLOWED to gamble money. Goodbye")
    quit()
else:
    print("Hello", userName + "!")

time.sleep(1)

#Rock/Paper/Scissors Game
option = input("Want to play me in rock paper scissors?")
match option:
        case "yes" | "Yes" | "y" | "YES" | "yeah" | "Yeah" | "YEAH" | "yea" | "Yea":
            time.sleep(1)
            print("Awesome! Let's get started.")
        case "no" | "No" | "n" | "NO" | "nope" | "Nope" | "NOPE":
            time.sleep(1)
            print("You said No!")
            quit()

def rock_paper_scissors():
    global moneyResult
    import time
    import string
    import random
    time.sleep(1)
    userSelection = input("Do you choose rock, paper, or scissors?")
    match userSelection:
            case "rock" | "ROCK" | "Rock":
                userSelection = "rock"
            case "paper" | "PAPER" | "Paper":
                userSelection = "paper"
            case "scissors" | "SCISSORS" | "Scissors":
                userSelection = "scissors"
    time.sleep(1)
    print("You chose", userSelection)
    rpsList = ['rock', 'paper', 'scissors']
    cpuSelection = random.choice(rpsList)
    time.sleep(2)
    print("I randomly selected:" ,cpuSelection)
#user selects rock
    if userSelection == "rock" and cpuSelection == "rock":
        endResult = "We tied! No one wins..."
        moneyResult = "tie"
    if userSelection == "rock" and cpuSelection == "paper":
        endResult = "Paper beats rock. I win!"
        moneyResult = "loss"
    if userSelection == "rock" and cpuSelection == "scissors":
        endResult = "Rock beats scissors. You win!"
        moneyResult = "win"
#user selects paper
    if userSelection == "paper" and cpuSelection == "rock":
        endResult = "Paper beats rock. You win!"
        moneyResult = "win"
    if userSelection == "paper" and cpuSelection == "paper":
        endResult = "We tied! No one wins..."
        moneyResult = "tie"
    if userSelection == "paper" and cpuSelection == "scissors":
        endResult = "Scissors beats paper. I win!"
        moneyResult = "loss"
#user selects scissors
    if userSelection == "scissors" and cpuSelection == "rock":
        endResult = "Rock beats scissors. I win!"
        moneyResult = "loss"
    if userSelection == "scissors" and cpuSelection == "paper":
        endResult = "Scissors beats paper. You win!"
        moneyResult = "win"
    if userSelection == "scissors" and cpuSelection == "scissors":
        endResult = "We tied! No one wins..."
        moneyResult = "tie"
    time.sleep(1)
    print(endResult)

def moneyCheck():
    import time
    global money
    time.sleep(1)
    print("You have $", money, "to spend.")

def wager():
    global money 
    global wagerAmount
    global updatedMoney
    wagerAmount = input("How much money would you like to wager?")
    wagerAmount = int(wagerAmount)
    updatedMoney = money - wagerAmount
    money = updatedMoney
    print("Your new bank balance is",money)

def wagerResult():
    import time
    global moneyResult
    global money
    global updatedMoney
    time.sleep(1)
    match moneyResult:
        case "win":
            print("You won", wagerAmount)
            money = money + (wagerAmount * 2)
        case "loss":
            print("You lost", wagerAmount)
        case "tie":
            print("You don't lose any money if we tie.")
            money = money + wagerAmount

moneyCheck()
wager()
rock_paper_scissors()
wagerResult()
moneyCheck()
while gameActive:
    playAgain = input("Would you like to play again?")
    match playAgain:
        case "yes" | "Yes" | "y" | "YES" | "yeah" | "Yeah" | "YEAH" | "yea" | "Yea":
            wager()
            rock_paper_scissors()
            wagerResult()
            moneyCheck()
        case "no" | "No" | "n" | "NO" | "nope" | "Nope" | "NOPE":
            print("Goodbye world")
            quit()
