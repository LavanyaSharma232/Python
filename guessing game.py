#guessing game
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a random number between 1 and {x} :"))
        if guess < random_number:
            print("Sorry, number too low. Guess again")
        elif guess > random_number:
            print("Sorry, number too high. Guess agin.")
    
    print(f"Yay, you guessed {random_number} correctly. Congratulations!")

guess(20)