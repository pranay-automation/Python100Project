import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

word_list = ["aasddbbb","ghfghf","hgjhgj"]


# TODO -1: - Create a variable called 'lives' to keep track of lives
#  Set 'lives' to equal 6

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeHolder=""
word_length = len(chosen_word)
for position in range(word_length):
    placeHolder += "_"
print(placeHolder)

#TODO 1 - Use a while loop to guess again
game_over = False
corrected_letter = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    #TODO -2: Change the for loop so that you keep the previous letters in display

    for letter in chosen_word:
        if letter == guess:
            display += letter
            corrected_letter.append(guess)
        elif letter in corrected_letter:
            display += letter
        else:
            display += "_"

    print(display)

#TODO 2: If guess is not a letter in the chosen word , then reduce 'lives' by 1
#  If lives goes down to 0 then the game should stop and it should  print "You lose"
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose")

    if "_" not in display:
        game_over = True
        print("You Win.")


# TODO 3: - print the ASCII art from "Stages"
#   That corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])