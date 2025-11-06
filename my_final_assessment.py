#I acknowledge the use of Microsoft Copilot ( https://copilot.microsoft.com/) to create the code in this file

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 10.")

# Track number of guesses
guess_count = 0

# Loop until the user guesses correctly
while True:
    guess = int(input("Take a guess: "))
    guess_count += 1
    
    if guess == secret_number:
        print(f"🎉 You guessed it! Well done in {guess_count} tries!")
        
        # Feedback based on performance
        if guess_count == 1:
            print("🏆 Incredible! You got it on the first try!")
        elif guess_count <= 3:
            print("👏 Great job! That was quick.")
        else:
            print("👍 Good effort! Practice makes perfect.")
        break
    elif guess < secret_number:
        print("🔼 Too low! Try again.")
    else:
        print("🔽 Too high! Try again.")
