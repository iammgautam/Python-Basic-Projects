# This program will help you to Guess whether the given input number is correct or not. k N
import random

def guess(x):
    random_number = random.randint(1,x)
    guess_number = 0
    while(guess_number != random_number):
        guess_number = int(input(f'Enter the number(between 1 and {x}):'))
        if guess_number > random_number:
            print("Guess is too high")
        elif guess_number < random_number:
            print("Guess is too low")
    print("Correct Guess")
    exit()

print(guess(10))