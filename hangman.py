"""Task 1: Hangman Game (CodeAlpha)"""
import random

WORDS = ["python", "internship", "variable", "function", "keyboard"]
MAX_WRONG = 6


def display_word(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong = 0

    print("=== HANGMAN ===")
    print(f"Guess the word. You can make {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        print("Word:", display_word(word, guessed))
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        print("Guessed letters:", " ".join(sorted(guessed)) or "-")

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.add(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            wrong += 1
            print("Wrong guess!\n")

        if all(letter in guessed for letter in word):
            print(f"You won! The word was '{word}'.")
            return

    print(f"Game over! The word was '{word}'.")


if __name__ == "__main__":
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
        print()
