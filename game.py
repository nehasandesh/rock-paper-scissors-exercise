


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

choices = ["rock", "paper", "scissors"]

#welcome message
print("------------------")
print("Welcome Player One to my Rock-Paper-Scissors game...")
print("------------------")


#ask for a user input

u = input("Please choose one: 'Rock', 'Paper', or 'Scissors':" )

#validations

u = u.lower()

if u in choices:
    print("User chose:", u)
else:
    print("You have entered an incorrect input and cannot continue playing, sorry!")
    exit()

#computer choice
    #using the random module (version 1)

import random

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)

print("Computer Chose:", computer_choice)
print("------------------")


#determine winner
#inspired from slack (eugenie) - nested if statements

if u == computer_choice:
    print("Both players chose", u , "It's a tie!")
elif u == "paper":
    if computer_choice == "rock":
        print("Paper covers rock. You won!")
    else:
        print("Scissors cut paper. You lost! It's okay.")
elif u == "rock":
    if computer_choice == "paper":
        print("Paper covers rock. You lost! It's okay.")
    else:
        print("Rock crushes scissors. You won!")
elif u == "scissors":
    if computer_choice == "paper":
        print("Scissors cut paper. You won!")
    else:
        print("Rock crushes scissors. You lost! It's okay.")

#final results

print("------------------")
print("Thanks for playing! Please play again!")