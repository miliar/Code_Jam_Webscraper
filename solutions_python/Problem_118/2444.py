#!/usr/bin/env python

import math
import sys
import numpy as np

from pprint import pprint


def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        t = int(lines[0])

        boards = []
        for i in range(1, t + 1):
            boards.append(map(int, lines[i].split()))

        return boards


def is_square(n):
    return math.sqrt(n) == round(math.sqrt(n))


def is_fair(n):
    s = str(n)
    r = str(int(math.sqrt(n)))
    return s == s[::-1] and r == r[::-1]


def build_numbers(a, b):
    f = np.vectorize(lambda n: int(is_square(n) and is_fair(n)))

    numbers = f(np.arange(0, b + 1))

    return numbers


def process(board, numbers):
    a, b = board
    s = numbers[a:b + 1]

    return np.sum(s)


boards = read_file(sys.argv[1])

minimum = min(map(min, boards))
maximum = max(map(max, boards))

numbers = build_numbers(minimum, maximum)

for i, board in enumerate(boards):
    result = process(board, numbers)
    print "Case #{0}: {1}".format(i + 1, result)
