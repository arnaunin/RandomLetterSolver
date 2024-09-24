import random as rd
import string as str
import time

counter = 0 # Generated word counter 
string = '' # Variable in which the generated word is stored
valid = False # Variable that checks if the word is valid

# Checks
while valid == False:
    word = input("Enter a word with a maximum of 5 letters: ")
    word = word.lower() # We convert all letters to lowercase
    if len(word) <= 5: # Lenght check
        for letter in word: # Check symbol by symbol if they are all letters
            if letter in str.ascii_lowercase:
                valid = True # While the checked symbols are letters, valid is True
            else: # If a symbol is not a letter
                print("ERROR: Invalid word.") # ERROR
                valid = False
                break # We go out of the loop
    else: # If the word has more than 5 symbols
        print("ERROR: Invalid word.")

# We show a waiting message since the execution may take a few seconds
print("Wait for the code to finish running.")
time.sleep(2)

# While loop to generate words and check if it is the entered word while the resulting word is not equal to the entered one
while string != word:
    counter += 1 # Counter update
    string = '' # We empty the variable since a new word is going to be generated

    # For loop to generate letters until the word is the length of the inserted word
    for i in range(len(word)):
        letter = rd.choice(str.ascii_lowercase) # Random lowercase letter
        string += letter # We add the letter to the string

# Output message
print(f"Attempts required to generate the word {word}: {counter}")
