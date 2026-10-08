"""CodeAlpha Task 1: Hangman Game"""
import random

WORDS = ["python", "program", "laptop", "internet", "keyboard"]
MAX_WRONG = 6


def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong = 0

    print("=== HANGMAN ===")
    print(f"Guess the word. You can make {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        display = " ".join(ch if ch in guessed else "_" for ch in word)
        print(f"Word: {display}")
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        print(f"Guessed letters: {' '.join(sorted(guessed)) or '-'}")

        if "_" not in display:
            print(f"\nYou won! The word was '{word}'.")
            return

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

    print(f"Game over! The word was '{word}'.")


if __name__ == "__main__":
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
