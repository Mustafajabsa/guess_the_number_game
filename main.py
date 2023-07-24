#Number Guessing Game Objectives:
from art import logo
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
print(logo)
print("Welcome to the number guess game!")
print("I'm thinking of number between 1 and 100.")

number = []
for i in range(1, 101):
        # to store all the optional numbers from 1 to 100
        number.append(i)
# to get one random number from the list of numbers
guess = random.choice(number)
def play():
        # function to start the game by asking the user to choose the level of difficulty
        global choice
        choice = input("choose a difficulty level: Type 'easy' or 'hard': ")
# where the game starts
play()
def hard():
        # the hard level
    attempts = 5
    global user_guess
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    while True:
            # loop to go through the attempts
        if attempts == 1:
            print("You've run out of guess! you lose.")
            break
        else:
            pass
        if user_guess > guess:
            attempts -= 1
            print("Too high.")
            print("guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))
        elif user_guess < guess:
            attempts -= 1
            print("Too low.")
            print("guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))
        elif user_guess == guess:
            print(f"You got it! the answer was {guess}")
            break
def easy():
        # the easy level
    attempts = 10
    global user_guess
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    while True:
            # while loop to go through the attempts
        if attempts == 1:
            print("You've run out of guess! you lose.")
            break
        else:
            pass
        if user_guess > guess:
            attempts -= 1
            print("Too high.")
            print("guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))
        elif user_guess < guess:
            attempts -= 1
            print("Too low.")
            print("guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))
        elif user_guess == guess:
            print(f"You got it! the answer was {guess}")
            break

# conditions to test the users choice
if choice == "hard":
    hard()
elif choice == "easy":
    easy()
else:
    print("invalied choice")
    play()