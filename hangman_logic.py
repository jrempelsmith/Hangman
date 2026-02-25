import input_validation
import wordlist
import random

def get_random_word(min_length, max_length):
    """
    Gets a word with a number of letters between min_length and max_length (both inclusive).

    Args:
        min_length (int): The minimum number of letters in the word that will be returned.
        max_length (int): The maximum number of letters in the word that will be returned.

    Returns:
        str: The randomly selected word with number of letters in the specified range.
    """
    word_list = wordlist.download_word_list()
    success = False
    while not success:
        random_word = random.choice(word_list)
        length = len(random_word)
        if length >= min_length and length <= max_length:
            return random_word.upper()


def get_valid_player_guess(guessed_letters):
    """
    Gets a single letter as input from the player. Ensures that the letter does not appear in guessed_letters.

    Args:
        guessed_letters (list of str): The list of letters that the player has guessed.

    Returns:
        str: The single letter that the player guesses.
    """
    success = False
    while not success:
        guess = input_validation.get_user_string("Enter a letter: ").upper()
        if len(guess) != 1:
            print("Must enter a single letter!")
        elif not guess.isalpha():
            print("Must enter a letter!")
        elif guess in guessed_letters:
            print(guess, "already guessed!")
        else:
            success = True
    
    return guess
        



def all_letters_are_revealed(hidden_word, guessed_letters):
    """
    Checks if all letters in hidden_word are present in guessed_letters.

    Args:
        hidden_word (str): The word the player is supposed to guess.
        guessed_letters (list of str): The list of letters that the player has guessed.

    Returns:
        bool: True if all letters in hidden_word are found in guessed_letters, False otherwise.
    """
    for letter in hidden_word:
        if letter.upper() not in guessed_letters:
            return False
    
    return True


if __name__ == "__main__":
    print(all_letters_are_revealed("hello", ["H", "L", "E", "O"]))
    
    

    
    
    
