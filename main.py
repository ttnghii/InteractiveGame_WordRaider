import random


# Build the word bank and reading it
with open('words.txt', 'r') as file:
    words = [line.strip().lower() for line in file]

bank = []
for word in words:
    bank.append(word)

word_to_guess = random.choice(bank)


# Variables to Track game state
misplaced_guesses, incorrect_guesses = [], []
max_turn = 5   # set defualt
current_turn = 0

## Print the current fame state
print('-'*10, 'Welcome to Word Raider game', '-'*10)
print('This word has', len(word_to_guess), 'letters.')
if (max_turn - current_turn) > 1: 
    print('Now, you have', max_turn - current_turn, 'turns left.')
else:
    print('Now, you have', max_turn - current_turn, 'turn left.')
