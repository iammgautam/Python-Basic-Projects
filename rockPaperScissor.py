#This program will you to play Rock Paper and Scisor with the Computer.

import random

def home():
    print("Welcome to the Rock Paper Scissor Game!!!\n")
    game()
    again()

def again():
    play_again = input("\nPress '1' to play again \n Press '0' to exit")
    if play_again == '1':
        game()
    elif play_again == '0':
        exit()
    else:
        print("Invalid Inputt!!!\nPress '1' or '0'.")
        again()


def game(): 
    print("Let's play the game.\n")
    user_choice = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissor(any one):")
    computer = random.choice(['r','p','s'])

    def draw():
        if user_choice == computer:
            print(f"You choose {user_choice} and Computer choose {computer}")
            return True
            
    def winner():
        if (user_choice =='r' and computer == 's') or (user_choice =='p' and computer == 'r') or (user_choice =='s' and computer == 'p'):
            print(f"You choose {user_choice} and Computer choose {computer}")
            return True

    def looser():
        if (user_choice =='r' and computer == 'p') or (user_choice =='p' and computer == 's') or (user_choice =='s' and computer == 'r'):
            print(f"You choose {user_choice} and Computer choose {computer}")
            return True

    if draw():
        print("It's a Tie!!")
        return again()
    if winner():
        print("YOU Won!! :))")
        return again()
    if looser():
        print('YOU Loose!! :((')
        return again()

home()