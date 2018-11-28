import os
import numpy as np
import scipy as sp
import sys
from sure import that
from itertools import combinations, permutations


input_file = open('input1.txt', 'r')
output_file = open('output1.txt', 'w')

T = int(input_file.readline().rstrip('\n'))
case_num = 1
while case_num - 1 < T:
    # Parse data
    data = map(int, input_file.readline().rstrip('\n').split(' '))
    typed = data[0]
    length = data[1]
    probs = map(float, input_file.readline().rstrip('\n').split(' '))
    assert that(len(probs)).equals(typed)

    enter = 1

    def product(probs):
        if not probs:
            return 1
        return reduce(lambda x, y: x * y, probs)
    
    def expected_strokes(typed, length):
        finish = length - typed + enter
        retype = finish + length + enter
        correct = product(probs[:typed])
        strokes = correct * finish + (1 - correct) * retype
        return strokes

    def get_min_backspace_stroke_count(typed, length):
        min_strokes = 99999999999999
        for backspaces in range(typed + 1):
            min_strokes = min(backspaces + expected_strokes(typed - backspaces, length), min_strokes)
        return min_strokes

    result = min(length + 2, get_min_backspace_stroke_count(typed, length))

    # Write result
    output_file.write('Case #{}: {}\n'.format(case_num, result))
    case_num += 1
