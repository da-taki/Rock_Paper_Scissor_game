#Importing the random library 
import random

#Setting up a score function
score = 0

#Setting up functions to either increase or decrease score
def change_score(won,score):
    if won:
        score +=1
    else:
        score -=1
    return score

#Starting a while loop so that the player can play the game n number of times
game_start = 1
while game_start == 1:
    #Exception Handling
    try:
        game_start = int(input("Do you want to play rock paper scissors(1=yes,0=no)?: "))
    except ValueError as e:
        print(e)
        print("Enter a number dum dum!")
        continue
    #Checking if they wanna play or not
    if game_start == 0:
        break
    #The enemies option selecting algorithm 
    enemy_options = ['Rock','Paper','Scissors']
    enemy_choice = random.choice(enemy_options)
    #Checking the player choice
    player_choice = input("Choose now!: ")
    #Going through every possible outcome
    if player_choice.lower() == enemy_choice.lower():
        print(f"Your enemy chose {enemy_choice}")
        print("Its a draw!")
    if player_choice.lower() == "rock":
        if enemy_choice.lower() == "paper":
            print(f"Your enemy chose {enemy_choice}")
            print("The enemy wins :(")
            score = change_score(False,score)
        if enemy_choice.lower() == "scissors":
            print(f"Your enemy chose {enemy_choice}")
            print("You WIN!")
            score = change_score(True,score)
    if player_choice.lower() == "paper":
        if enemy_choice.lower() == "rock":
            print(f"Your enemy chose {enemy_choice}")
            print("You WIN!")
            score = change_score(True,score)
        if enemy_choice.lower() == "scissors":
            print(f"Your enemy chose {enemy_choice}")
            print("You lose :(")
            score = change_score(False,score)
    if player_choice.lower() == "scissors" or player_choice.lower() == "scissor":
        if enemy_choice.lower() == "rock":
            print(f"Your enemy chose {enemy_choice}")
            print("You lose :(")
            score = change_score(False,score)
        if enemy_choice.lower() == "paper":
            print(f"Your enemy chose {enemy_choice}")
            print("You win!")
            score = change_score(True,score)

    #Exception Handling
    if player_choice.lower() != "rock" and player_choice.lower() != "paper" and player_choice.lower() != "scissors" and player_choice.lower() != "scissor":
        print("Chose either Rock, Paper or Scissor dum dum!")
        continue

    #Displaying the players Score
    print(f"Your Score is: {score}")
    