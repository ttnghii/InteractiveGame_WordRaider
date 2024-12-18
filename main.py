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
max_turns = 5   # set defualt
total_turns = 0


# Print the current fame state
print('-'*10, '🎉 Welcome to Word Raider game 🎉', '-'*10)
print(f'❗You need to guess a {len(word_to_guess)} letters word, food-themed.')
print('\t❗You have', max_turns - total_turns, 'turns to guess. Good luck 💛')


# The game loop
while total_turns < max_turns:
    # Get the player's guess
    print(f'\nTurn {total_turns + 1}:')
    guess = input('\tYour guess: ').lower()

    # Check the valid word's length (defualt = 5)
    if (len(guess) != len(word_to_guess)) or (not guess.isalpha()):
        print('\tPlease enter the 5-letter word!')
        continue

    # Classify the guess word
    index = 0
    for letter in guess:
        # Guess letter is both correct character and position
        if letter == word_to_guess[index]:
            print(letter, end=' ')
            if letter in misplaced_guesses:
                misplaced_guesses.remove(letter)
        # Guess letter is correct character but places in wrong position
        elif letter in word_to_guess:
            if letter not in misplaced_guesses:
                misplaced_guesses.append(letter)
            print('_', end=' ')
        # Guess letter is wrong
        else:
            if letter not in incorrect_guesses:
                incorrect_guesses.append(letter)
            print('_', end=' ')
        index += 1

    # End of this turn
    print('\n\tMisplaced letters: ', misplaced_guesses)
    print('\tIncorrect letters: ', incorrect_guesses)
    total_turns += 1


    # Check the player's result
    ## If the player are the winner
    if guess == word_to_guess:
        print('🥇'*10, 'CONGRATULATIONS! YOU ARE THE WINNER, WEAR YOUR CROWN 👑', '🥇'*10)
        break

    ## If the player has lost
    if total_turns == max_turns:
        print('💀'*10, 'YOU LOST. THE WORD WAS', word_to_guess.upper(), '😜', '💀'*10)
        break