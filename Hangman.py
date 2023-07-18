# Determination of difficulty:
# 1 - European countries and capitals
# 2 - countries and capitals of the world

# Importing the random module, pictogram file and color class

import random
from hangmanpics import HANGMANPICS
from colors import color
import os# dobrze wyciagac tylko fragment


# Function description

def file_handle(l):#
    file = open(l, "r", encoding="utf-8") 
    contents = file.read() 
    list = contents.split("\n")#readlines
    file.close()
    return list


def printing_current_status(d):#dłuższe nazwy, nie d
    difficulty = d    
    if difficulty == 1:
        print(color.OKGREEN + "Guessed word is country or capital city of Europe" + color.ENDC)
    elif difficulty == 2:
        print(color.OKGREEN + "Guessed word is country or capital city of the world" + color.ENDC)
    print(color.OKBLUE + HANGMANPICS[6-(difficulty*life_number)] + color.ENDC)
    print("\n"f"Number of lives = {life_number}")
    print(f"Wrong guesses: {miss_letters}""\n")

    game_state = ""

    for i in word:# I change name of variable from "letter" for "i", because it might be confusing with name of variable "letter" from input
        if i in letters_guessed and i == word[0]:
            game_state += i.upper() + " "
        elif i in letters_guessed:
            game_state += i + " "
        elif i == " ":
            game_state += " "
        else:
            game_state += "_ "


    print(game_state)
    return game_state

again = 1
while again == 1:



# Create variables

    letters_guessed = []
    miss_letters = []
    life_number = None
    difficulty = None


# The actual part of the program.
# The first while loop is related to choosing the difficulty level and communicating what the player has to guess.
# The loop will keep asking the player until he gives a 1 or 2.

    print("\nWelcome to Hangman!\nLet's start by choosing a difficulty level, where:\n1 - Country or capital city of Europe\n2 - Country or capital city of the world\n3 - Close App")

    while True: #funkcja
        difficulty_level = input("\nPick a number and click 'Enter' (1,2 or 3): ")
        if difficulty_level == "1":
            list = file_handle("Country or capital city of Europe.txt")
            os.system('cls')
            print(color.OKGREEN + "Guessed word is country or capital city of Europe" + color.ENDC)
            difficulty = 1
            life_number = 6
            break
        elif difficulty_level == "2":
            list = file_handle("Country or capital city of the world.txt")
            os.system('cls')
            print(color.OKGREEN + "Guessed word is country or capital city of the world" + color.ENDC)
            difficulty = 2
            life_number = 3
            break
        elif difficulty_level == "3":
            break

    if difficulty_level == "3":
        os.system('cls')
        print(color.FAIL + "\n""Goodbye" + color.ENDC)
        break
                
                    
            
            
# Randomizing a word from the range of available words and determining the number of letters in the password

    word = random.choice(list)
                              
# Main loop
# The second while loop runs as long as you are playing the game, asks the player for a letter, prints the current state of the game in the terminal,
# protects against entering a number or an incorrect combination of characters, displays all information. 

    for i in word:#letter
        if i == " ":
            print("  ", end = "")
        else:
            print("_ ", end = "")


    while True:
        letter = input(color.OKGREEN + "\n\n""Guess a letter (or type 'quit' to exit): " + color.ENDC)
        os.system('cls')

        if letter == "quit":
            print(color.FAIL + "\n""Goodbye" + color.ENDC)
            break
    
        if len(letter) != 1 or letter.isalpha() == False:
            print(color.FAIL + "You entered wrong combination" + color.ENDC)
            printing_current_status(difficulty)
            continue

        if letter.lower() in miss_letters or letter.lower() in letters_guessed:
            print(color.FAIL + "You've already guessed that letter." + color.ENDC)
            printing_current_status(difficulty)
            continue

        if letter.lower() in word or letter.upper() in word :
            letters_guessed.append(letter.lower())
            letters_guessed.append(letter.upper())
        else:
            miss_letters.append(letter.lower())
            life_number -= 1

        game_state = printing_current_status(difficulty)
        if "_" not in game_state:
            print(color.OKGREEN + "\nCongratulations! You won!\n" + color.ENDC)

        if life_number == 0 or "_" not in game_state:    
            if life_number == 0:
                print(color.FAIL + "\n\n"f"Game over! You lost. The word was: {word.upper()}""\n\n" + color.ENDC)
            while again != 1 or again != 2:
                again = input(color.OKBLUE + "Do you want to Try Again?:(1:Yes/2:No) " + color.ENDC)
                if again == "1":
                    again = 1
                    os.system('cls')
                    break
                elif again == "2":
                    again = 2
                    os.system('cls')
                    print(color.FAIL + "\n""Goodbye" + color.ENDC)
                    break
            break
    if letter == "quit":
        break

input()

#za mało funkcji, duzo powtarzalnego kodu, brak nazywania jednoliterowego, brak booli, np. again