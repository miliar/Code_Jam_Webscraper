#!/usr/bin/python

import sys
import string

def read_file(file_name):
    f = open(file_name, 'r')
    text = f.read()
    f.close()

    return text

def guess_a_game(text):

    text_by_line = string.split(text, '\n')
    num_test_cases = text_by_line[0]
    current_line = 1

    for test in xrange(int(num_test_cases)):
        first_input = int(text_by_line[current_line])
        current_line += 1

        # find which row the first_input is contained in
        row_index = current_line + (first_input - 1)
        possible_numbers = string.split(text_by_line[row_index])

        current_line += 4

        # now parse the second arrangement
        second_input = int(text_by_line[current_line])
        current_line += 1

        row_index = current_line + (second_input - 1)
        possible_numbers2 = string.split(text_by_line[row_index])

        current_line += 4

        # check the intersection between possible_numbers and possible_numbers2
        final_guesses = []
        for i in possible_numbers:
            if i in possible_numbers2:
                final_guesses.append(i)

        if len(final_guesses) == 1:
            result = str(final_guesses[0])

        elif len(final_guesses) > 1:
            result = 'Bad magician!'
        else:
            result = 'Volunteer cheated!'

        print 'Case #%d: %s' % (test+1, result)

def main():
    text_file = sys.argv[1]
    parsed_text = read_file(text_file)

    guess_a_game(parsed_text)

if __name__ == '__main__':
    main()
