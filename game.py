


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#




#ask for a user input

u = input("Please choose one: Rock, Paper, or Scissors:")

print("User chose:", u)

#validations



#computer choice
    #using the random module (version 1)

import random

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)

print("Computer Chose:", computer_choice)


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