with open('words.txt', 'r') as file:
    words = [line.strip() for line in file]

# Create an empty list to conserve all words
bank = []
for word in words:
    bank.append(word)