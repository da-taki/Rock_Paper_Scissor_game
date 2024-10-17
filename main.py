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
    game_start = int(input("Do you want to play rock paper scissors(1=yes,0=no)?: "))
    if game_start == 0:
        break
    enemy_options = ['Rock','Paper','Scissors']
    enemy_choice = random.choice(enemy_options)

    player_choice = input("Choose now!: ")

    if player_choice.lower() == "rock" and enemy_choice.lower() == "rock":
        print(f"Your enemy chose {enemy_choice}")
        print("Its a draw!")
    if player_choice.lower() == "rock" and enemy_choice.lower() == "paper":
        print(f"Your enemy chose {enemy_choice}")
        print("The enemy wins :(")
        score = change_score(False,score)
    if player_choice.lower() == "rock" and enemy_choice.lower() == "scissors":
        print(f"Your enemy chose {enemy_choice}")
        print("You WIN!")
        score = change_score(True,score)
    if player_choice.lower() == "paper" and enemy_choice.lower() == "rock":
        print(f"Your enemy chose {enemy_choice}")
        print("You WIN!")
        score = change_score(True,score)
    if player_choice.lower() == "paper" and enemy_choice.lower() == "paper":
        print(f"Your enemy chose {enemy_choice}")
        print("Its a draw!")
    if player_choice.lower() == "paper" and enemy_choice.lower() == "scissors":
        print(f"Your enemy chose {enemy_choice}")
        print("You lose :(")
        score = change_score(False,score)
    if player_choice.lower() == "scissors" and enemy_choice.lower() == "rock":
        print(f"Your enemy chose {enemy_choice}")
        print("You lose :(")
        score = change_score(False,score)
    if player_choice.lower() == "scissors" and enemy_choice.lower() == "paper":
        print(f"Your enemy chose {enemy_choice}")
        print("You win!")
        score = change_score(True,score)
    if player_choice.lower() == "scissors" and enemy_choice.lower() == "scissors":
        print(f"Your enemy chose {enemy_choice}")
        print("Its a draw!")
    print(f"Your Score is: {score}")
    