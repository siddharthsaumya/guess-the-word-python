import random

temp = 0
words = [
    "apple", "orange", "pokemon", "noodles", "chicken", "food", "mobile",
    "computer"
]
word = random.choice(words)
word_length = len(word)
master_word = ""
for n in range(0, word_length):
    master_word = master_word[:n] + "-"
print("Guess what the word is?!\nWord has " + str(word_length) +
      " charecters.\n")
for m in range(0, word_length):
    print("\nYour word now looks like: " + master_word)
    guessed_alphabet = input("Enter the alphabet you guessed? ")
    for x in range(0, word_length):
        if guessed_alphabet == word[x]:
            master_word = master_word[:x] + guessed_alphabet + master_word[x +
                                                                           1:]
if master_word != word:
    print("\nYou Loose :(\nAnswer was: " + word)
else:
    print("\nYou Won :)\nAnswer was: " + word)
