
import random

words = ["python", "computer", "mobile", "apple", "school"]

secret_word = random.choice(words)
guessed_letters = []
wrong_attempts = 0
max_attempts = 6

print("\n===== WELCOME TO HANGMAN =====")

while wrong_attempts < max_attempts:

    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong attempts:", wrong_attempts, "/", max_attempts)

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You Won!")
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet!")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_attempts += 1
        print("Wrong guess!")

else:
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)

print("\nThanks for playing Hangman!")
