# coding: utf8

import sys
import math
from collections import defaultdict


OUTPUT_TEMPLATE = 'Case #{0}: {1}\n'


def is_palindrome(num):
    s_num = str(num)

    return s_num == s_num[::-1]


def is_fair(num):
    return is_palindrome(num)


def is_square(num):
    sqrt_of_num = math.sqrt(num)

    return is_palindrome(int(sqrt_of_num)) if sqrt_of_num.is_integer() else False


def is_fair_and_square(num):
    return is_fair(num) and is_square(num)


if __name__ == '__main__':
    # Not the most optimal solution in the history of the most optimal solutions
    fp = open(sys.argv[1], 'rb')

    number_of_cases = int(fp.readline())
    solutions = defaultdict(int)

    for case in xrange(1, number_of_cases + 1):
        start, stop = map(int, fp.readline().split())

        for num in xrange(start, stop + 1):
            if is_palindrome(num):
                if is_fair_and_square(num):
                    solutions[case] += 1

        if case not in solutions:
            solutions[case] = 0

    fp.close()

    output = open('output.txt', 'ab')

    for case, num_of_solutions in solutions.iteritems():
        output.write(OUTPUT_TEMPLATE.format(case, num_of_solutions))

    output.close()
