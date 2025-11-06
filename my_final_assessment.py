#I acknowledge the use of Microsoft Copilot ( https://copilot.microsoft.com/) to create the code in this file

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 10.")

# Loop until the user guesses correctly
while True:
    guess = int(input("Take a guess: "))
    
    if guess == secret_number:
        print("🎉 You guessed it! Well done!")
        break
    elif guess < secret_number:
        print("🔼 Too low! Try again.")
    else:
        print("🔽 Too high! Try again.")
