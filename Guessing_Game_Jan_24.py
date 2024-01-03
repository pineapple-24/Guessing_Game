#Brandon Thompson Jan 2024
#Guessing Game
#email is brandon2093@hotmail dot com

################################################
#Table of Contents
#1) import module section
#2) formula section


################################################
#1 import section
import random as rd

################################################
#2) formula for the guessing game
def main():
    print("Welcome to the Guessing Game")
    print("lowest number will be 1")
    print("highest number will be up to you")
    print("I will tell you if you are too high or too low")
    print("how high do you want to go?")
    high_num = eval(input("Enter the highest number to start: "))
    number = rd.randint(1, high_num)
    guess = 0
    count = 0
    print("Now lets begin the game")
    print("-"*40)
    while guess != number:
        guess = eval(input("Enter a number: "))
        count = count + 1
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            print("You guessed it in", count, "tries.\n")
            print("Thanks for playing the Guessing Game")
            print("Created by Brandon Thompson")

main()

