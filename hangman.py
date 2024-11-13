import random
HANGMAN_PICS = [
    """
     ------
    ----------------------------
     |                      |
     |                      
     |                     
     |   
     |      
    ---""",
    """
     ----------------------------
     |                      |
     |                      O
     |                     
     |   
     |      
    ---""",
    """
     ----------------------------
     |                      |
     |                      O
     |                      |
     |
     |   
     |     
    ---""",
    """
     ----------------------------
     |                      |
     |                      O
     |                     /|
     |   
     |   
    ---""",
    """
    ----------------------------
     |                      |
     |                      O
     |                     /|\\
     |   
     |   
    ---""",
    """
    ----------------------------
     |                      |
     |                      O
     |                     /|\\
     |                     /
     |   
    ---""",
    """
     ----------------------------
     |                      |
     |                      O
     |                     /|\\
     |                     / \\
     |  
    ---"""
]

def hangman():
    word_list = ["python", "java", "ruby", "javascript", "hangman", "coding", "programming"]
    word = random.choice(word_list).lower()
    guessed = []
    attempts = 6
    correct_guesses = 0

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0 and correct_guesses < len(word):
        print(HANGMAN_PICS[6 - attempts])  # Display the current hangman stage based on attempts left
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You've already guessed that letter.")
            continue

        guessed.append(guess)

        if guess in word:
            correct_guesses += word.count(guess)
            print(f"Good guess: {guess}")
        else:
            attempts -= 1
            print(f"Sorry, {guess} is not in the word. You have {attempts} attempts left.")

        # Display current state of the word
        display_word = ''.join([letter if letter in guessed else '_' for letter in word])
        print("Current word: " + ' '.join(display_word))

    # Final result
    if correct_guesses == len(word):
        print(f"Congratulations! You've guessed the word '{word}'!")
    else:
        print(HANGMAN_PICS[-1])  # Display the final hangman stage
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
