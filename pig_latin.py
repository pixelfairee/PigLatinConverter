##Python 3.7.5

import re

VOWELS = ['a', 'e', 'i', 'o','u']
TAIL = 'ay'

def translate(words):
    """ Function to translate a word or phrase to Pig Latin"""

    new_list = []   # List of converted words to Pig Latin
    for word in words.split():
        # Get index of the first vowel in each word
        first_vowel_idx = re.search("[aeiou]", word, re.IGNORECASE)

        # if word begins with a vowel
        if first_vowel_idx.start() == 0:
            new_list.append(word + TAIL)
        # else if word begins qu
        elif word[first_vowel_idx.start()] == 'u' and word[first_vowel_idx.start() - 1] == 'q':
            new_list.append(word[first_vowel_idx.start() + 1:] + word[:first_vowel_idx.start() + 1] + TAIL)
            #else if word begins consonant
        else:
            new_list.append(word[first_vowel_idx.start():] + word[:first_vowel_idx.start()] + TAIL)

    return " ".join(new_list)

