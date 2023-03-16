import random

computer_Score = 0
player_Score = 0

while True:
    print("We are going to play rock, paper, scissors, your score is", player_Score, "and the computer's score is", str(computer_Score)+".")
    if computer_Score == player_Score:
        print("You are tied.")
    elif computer_Score > player_Score:
        print("The computer is in the lead")
    elif computer_Score < player_Score:
        print("You are in the lead!")
    player_Input = str(input("Enter your weapon of choice "))
    weapons = ["rock", "paper", "scissors"]
    computer_Choice = random.choice(weapons)
    print("You chose", player_Input, "and the computer chose", computer_Choice+".")
    player_Choice = player_Input.lower()

    if computer_Choice == player_Choice:
        print("It's a tie!")
    elif player_Choice == "rock":
        if computer_Choice == "scissors":
            print("Well done, you win!")
            player_Score += 1
        else:
            print("Computer wins, better luck next time.")
        computer_Score += 1
    elif player_Choice == "paper":
        if computer_Choice == "rock":
            print("Well done, you win!")
            player_Score += 1
        else:
            print("Computer wins, better luck next time.")
            computer_Score += 1
    elif player_Choice == "scissors":
        if computer_Choice == "paper":
            print("Well done, you win!")
            player_Score += 1
        else:
            print("Computer wins, better luck next time.")
            computer_Score += 1
    continue_Playing = str(input("Would you like to play? y/n "))
    if continue_Playing.lower() == "n":
        break


