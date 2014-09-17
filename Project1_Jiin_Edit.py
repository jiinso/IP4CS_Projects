# Project 1: Rock, Paper, Scissors, Lizard, Spock!
# Author: jiinso
# Date: 9/16/2014
# Purpose: This code is to play Rock, Paper, Scissors, Lizard, Spock with your computer!
# This is a project assigned in the course PHY 371: Intro to Programming for Computational Physics (IP4CS).
# This course is offered as a special topic in the physics department of Gordon College in Fall 2014.


# Import needed functions
# The random.choice function will allow the computer to generate a random choice.
# The exit function from the package sys will allow us to exit from the script file once we are done playing the game.
from random import choice
from sys import exit


# Give the explanation of the game rules and print it out for the user to see.
game_rules = ("""
The rules of rock-paper-scissors-lizard-Spock are:
    - scissors cut paper
    - paper covers rock
    - rock crushes lizard
    - lizard poisons Spock
    - Spock smashes scissors
    - scissors decapitate lizard
    - lizard eats paper
    - paper disproves Spock
    - Spock vaporizes rock
    - rock crushes scissors.

You will be playing against me, the computer.
""")
print game_rules

# Create a loop so that the script keeps running on and on unless done = True, so that while not done = False.
# Once the redefining of done = True and while not done = False occurs, the loop will stop.
done = False
while not done:

    # Ask the user to input an option of their choice and set it to the variable user. It will be a string.
    user = raw_input('''You have five options: rock, paper, scissors, lizard, or Spock.
Type in your decision: ''')
    
    # If the input from the user is not one of the five options, show an error message and ask for an acceptable input.
    while user != "rock" and user != "paper" and user != "scissors" and user != "lizard" and user != "Spock":
        user = raw_input('''ERROR! You did not chose one of the five available options.
Please choose between rock, paper, scissors, lizard, or Spock: ''')

    # Create a list of the options we have. 			
    options = ['rock', 'paper', 'scissors', 'lizard', 'Spock']

	# Assign a random choice to 'computer' by randomly choosing an item in the list 'options'
	# Note that since this is inside the 'while not done' loop, each time the user plays again the variable 'computer' will receive a new assignment.
    computer = choice(options)
	
	# Use the game rules to create conditional statements that compare the user option with the computer option.
	# First break it up into the five possibilities of the user's choice.
	# Then write nested if-elif statements for each computer choice (5 of them) in each of the five possibilities.
	# Print the user choice and the computer choice and announce the winner accordingly. Here "I" is the computer, and "you" is the user.
	# If the user choice is the same as the computer choice a tie is announced.
	# %s are used to input the user choice or the computer choice into the printed string.
	# %s this helps to avoid spelling mistakes and other mix-ups since we are pulling directly from the variable and not writing the choice out.
	# When user chooses rock
    if user == 'rock':
    	if computer == user:
            print 'We both chose %s. It is a tie.' % (computer)
        elif computer == 'paper':
            print 'You chose %s and I chose %s. I win!' % (user, computer)
        elif computer == 'scissors':
            print 'You chose %s and I chose %s. You win!' % (user, computer)
        elif computer == 'lizard':
            print 'You chose %s and I chose %s. You win!'% (user, computer)
        elif computer == 'Spock':
    	    print 'You chose %s and I chose %s. I win!' % (user, computer)
    # When user chooses scissors
    elif user == 'scissors':
        if computer == user:
            print ('We both chose %s. It is a tie.' % (computer))
        elif computer == 'paper':
            print ('You chose %s and I chose %s. You win!' % (user, computer))
        elif computer == 'rock':
            print ('You chose %s and I chose %s. I win!' % (user, computer))
        elif computer == 'lizard':
    	    print ('You chose %s and I chose %s. You win!' % (user, computer))
        elif computer == 'Spock':
            print ('You chose %s and I chose %s. I win!' % (user, computer))
    # When user chooses paper
    elif user == 'paper':
        if computer == user:
            print ('We both chose %s. It is a tie.' % (computer))
        elif computer == 'rock':
            print ('You chose %s and I chose %s. You win!' % (user, computer))
        elif computer == 'scissors':
            print ('You chose %s and I chose %s. I win!' % (user, computer))
        elif computer == 'lizard':
	    print ('You chose %s and I chose %s. I win!' % (user, computer))
        elif computer == 'Spock':
            print ('You chose %s and I chose %s. You win!' % (user, computer))
    # When user chooses lizard
    elif user == 'lizard':
        if computer == user:
            print ('We both chose %s. It is a tie.' % (computer))
        elif computer == 'paper':
            print ('You chose %s and I chose %s. You win!' % (user, computer))
        elif computer == 'scissors':
            print ('You chose %s and I chose %s. I win!' % (user, computer))
        elif computer == 'rock':
            print ('You chose %s and I chose %s. I win!' % (user, computer))
        elif computer == 'Spock':
            print ('You chose %s and I chose %s. You win!' % (user, computer))
    # When user chooses Spock
    elif user == 'Spock':
        if computer == user:
            print ('We both chose %s. It is a tie.' % (computer))
        elif computer == 'paper':
            print ('You chose %s and I chose %s. I win!' % (user, computer))
        elif computer == 'scissors':
            print ('You chose %s and I chose %s. You win!' % (user, computer))
        elif computer == 'lizard':
            print ('You chose %s and I chose %s. I win!' % (user, computer))
        elif computer == 'rock':
            print ('You chose %s and I chose %s. You win!' % (user, computer))
    
    
    # Note that the blank print function below and the following blank functions are meant to be for aesthetic purposes.
    # With the blank lines the running script is easier for the user to read (and less crowded).
    print
    
    # Ask the user if they want to play again.
    # The input should be type string, and answered either 'yes' or 'no'
    answer = raw_input('Do you want to play again? ')
    
    # The following function play_again takes the user's answer and determines if the 'while not done' loop will continue or stop.
    # It takes one argument x.
    def play_again(answer):
        while answer!= 'yes' and answer != 'no':
            answer = raw_input('I did not quite catch that. Please answer yes or no: ')
        if answer == "yes":
            print
            print ('Great! Let us play another round! :) ')
            print
        elif answer =='no':
            print
            print ('Thanks for playing! Goodbye.')
            print
            # If the user answers no, redefine done = True to stop the 'while not done loop' 
            done = True
            # Since the user does not want to play the game anymore, exit the script.
            exit ()
            
            
    # Call the function using the argument answer in place of x
    play_again(answer)


