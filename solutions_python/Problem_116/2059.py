#!/usr/bin/python3.3

import itertools
import numpy as np
import pprint
import sys


def decide(lines):
    for line in lines:
        if all(el in 'XT' for el in line):
            return 'X won'
        elif all(el in 'OT' for el in line):
            return 'O won'
    if '.' in lines:
        return 'Game has not completed'
    else:
        return 'Draw'

def antidiagonal(m4):
    # http://math.jacobs-university.de/oliver/teaching/numpy-intro/numpy-intro/
    i = np.arange(4)
    j = i[::-1]
    return m4[i, j]


inputs = int(sys.stdin.readline())


for i in range(inputs):
    board = []
    for line in itertools.islice(sys.stdin, 5):
        board.extend(line.rstrip())
    arr = np.array(board)
    arr.shape = (4, 4)
    at = arr.transpose()
    lines = np.concatenate((arr, at, [arr.diagonal()], [antidiagonal(at)]))
    #print(arr); print(lines)
    win = decide(lines)
    print('Case #{}: {}'.format(i + 1, win))


