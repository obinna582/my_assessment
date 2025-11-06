#I acknowledge the use of Microsoft Copilot ( https://copilot.microsoft.com/) to create the code in this file

import random
import tkinter as tk
from tkinter import messagebox

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
guess_count = 0

# Function to check the guess
def check_guess():
    global guess_count
    try:
        guess = int(entry.get())
        guess_count += 1
        if guess == secret_number:
            message = f"🎉 You guessed it in {guess_count} tries!\n"
            if guess_count == 1:
                message += "🏆 Incredible! You got it on the first try!"
            elif guess_count <= 3:
                message += "👏 Great job! That was quick."
            else:
                message += "👍 Good effort! Practice makes perfect."
            messagebox.showinfo("Correct!", message)
            root.destroy()
        elif guess < secret_number:
            feedback_label.config(text="🔼 Too low! Try again.")
        else:
            feedback_label.config(text="🔽 Too high! Try again.")
    except ValueError:
        feedback_label.config(text="⚠️ Please enter a valid number.")

# Set up the GUI window
root = tk.Tk()
root.title("Guess the Number Game")

tk.Label(root, text="I'm thinking of a number between 1 and 10.").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)
entry.focus()  # 👈 This sets focus to the entry box

tk.Button(root, text="Guess", command=check_guess).pack(pady=5)
feedback_label = tk.Label(root, text="")
feedback_label.pack(pady=10)

root.mainloop()
