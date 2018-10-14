#! /usr/bin/env python

import pprint
import sys

def count_possibilities(language, test_string):
    letter_count = 0
    return_count = 0

    if test_string[letter_count] == '(':
        paren_string = ""
        letter_count += 1
        while  test_string[letter_count] != ')':
            paren_string += test_string[letter_count]
            letter_count += 1
    else:
        paren_string = test_string[letter_count]

    letter_count += 1

    for letter in paren_string:
        if language.has_key(letter):
            if language[letter].has_key('word'):
                return 1
            else:
                return_count += count_possibilities(language[letter],
                                                    test_string[letter_count:])
    return return_count
        

if __name__ == "__main__":

    data = open(sys.argv[1])

    params = data.readline().strip().split()

    word_len = int(params[0])
    lang_len = int(params[1])
    cases = int(params[2])


    language = {}
    for count in range(0, lang_len):
        word = data.readline().strip()

        letter_pointer = language
        for letter in word:
            if not letter_pointer.has_key(letter):
                letter_pointer[letter] = {}
            letter_pointer = letter_pointer[letter]
        letter_pointer['word'] = word

    for i in (range(1, cases + 1)):
        print ("Case #%s: %s" % (i,
                                 count_possibilities(language, data.readline().strip()))
        )

