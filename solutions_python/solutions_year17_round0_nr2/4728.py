#!/usr/bin/env python

import collections
import math
import sys

def nines(number_string):
    number = int(number_string)
    return (10**int(math.log10(number))) - 1

assert nines(10) == 9
assert nines(1000) == 999

def is_tidy(number):
    digits = [int(d) for d in str(number)]
    previous = 0
    for digit in digits:
        if digit >= previous:
            previous = digit
        else:
            return False
    return True

assert is_tidy(123)
assert not is_tidy(121)

def solve(number_string):
#    if '0' in number_string:
#        return nines(number_string)

    number = int(number_string)

    while not is_tidy(number):
        number -= 1

    return number


input_lines = [l for l in open(sys.argv[1]).read().split('\n') if l]
input_lines = input_lines[1:]
for case, input_line in enumerate(input_lines):
    solution = solve(input_line)
    print "Case #{case}: {solution}".format(
        case=case + 1,
        solution=solution
    )
