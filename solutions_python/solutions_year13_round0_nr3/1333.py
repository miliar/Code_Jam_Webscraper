
import sys
import os

import numpy as np

def get_squares(start, end):
    first = int(np.ceil(np.sqrt(start)))
    last = int(np.floor(np.sqrt(end)))

    return list(range(first, last + 1))

def get_palindromes(list):
    pals = []
    for xi in list:
        str_xi = str(xi)
        mid = len(str_xi) / 2
        left = int(np.floor(mid))
        right = int(np.ceil(mid))
        if len(str_xi) == 1 or (str_xi[:left] == str_xi[right:]):
            pals.append(xi)
    return pals

filename = sys.argv[1]

input_file = open(filename, 'r')
output_file = open(os.path.splitext(filename)[0] + '.out', 'w')

input_lines = input_file.readlines()
num_cases = int(input_lines[0])

next_line = 1
for case_i in range(num_cases):
    range_str = input_lines[next_line].strip('\n').split(' ')
    start, end = int(range_str[0]), int(range_str[1])
    next_line += 1

    #before even checking for palindromes, we should check for square numbers that are palindromes
    #in the given range
    squares = get_squares(start, end)
    #print(squares)

    square_palindromes = np.array(get_palindromes(squares))

    fair_and_square = get_palindromes(square_palindromes * square_palindromes)

    result = len(fair_and_square)
    #print(fair_and_square)
    #print(result)
    output_file.write('Case #%i: %s\n' % (case_i + 1, result))

output_file.close()