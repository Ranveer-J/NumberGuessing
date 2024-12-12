import random

def number_guessing_game():
    numbers = [10, 20, 30, 40, 50]  
    secret_number = random.choice(numbers)
    print("Try to guess my number!")

    while True:
        guess = int(input("Guess a number (10, 20, 30, 40, 50): "))
        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print("Correct!")
            break