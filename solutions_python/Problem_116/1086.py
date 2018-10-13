#!/usr/bin/env python

from __future__ import print_function
import pprint
import re
from operator import itemgetter
import timeit

def slowtranspose(string, cols=4):
    """ transpose a string representing a cols x cols matrix (1M/22s)"""
    transposed = []
    for c in range(1, cols + 1):
        for i, char in enumerate(string, start=1):
            if (i - 1) % cols + 1 == c:
                transposed.append(char)
    return ''.join(transposed)

def listtranspose(string, cols=4):
    """ transpose a string representing a cols x cols matrix (1M/9.6s)"""
    transposed = []
    for column in range(cols):
        getter = itemgetter(*[ (i * cols) + column for i in range(cols) ])
        transposed += getter(string)
    return ''.join(transposed)

def transpose(string, cols=4):
    """ transpose a string representing a cols x cols matrix (1M/9.1s)"""
    transposed = ''
    for column in range(cols):
        getter = itemgetter(*[ (i * cols) + column for i in range(cols) ])
        transposed += ''.join(getter(string))
    return transposed

def straight(game, side='X', cols=4):
    """ check if game has a horizontal win for side ``side`` """
    pattern = re.compile('(%s|T){%s,%s}' % (side, cols, cols))
    rows = int(len(game) / cols)
    won = False
    for row in range(rows):
        getter = itemgetter(*[ (row * cols) + i for i in range(cols) ])
        won = bool(re.search(pattern, ''.join(getter(game))))
        if won:
            break
    return won

def diagonal(game, side='X', cols=4):
    """ check for a diagonal win of side ``side`` """
    # top-left => bottom-right
    pattern = re.compile('(%s|T){%s,%s}' % (side, cols, cols))

    getter = itemgetter(*[ i * (cols + 1) for i in range(cols) ])
    tlbr = bool(re.match(pattern, ''.join(getter(game))))

    # top-right => bottom-left
    getter = itemgetter(*[ (i + 1) * (cols - 1) for i in range(cols) ])
    trbl = bool(re.match(pattern, ''.join(getter(game))))

    return tlbr or trbl

def main(filename):
    # def cases
    cases = []
    with open(filename, 'r') as handle:
        for i, line in enumerate(handle):
            if i % 5 == 1:
                # fresh case
                case = ''
                case += line.strip()
            if i % 5 == 2:
                case += line.strip()
            if i % 5 == 3:
                case += line.strip()
            if i % 5 == 4:
                case += line.strip()
                # wrap up
                cases.append(case)

    # pprint.pprint(cases)
    # print(transpose(cases[0]))
    # print(slowtranspose(cases[0]))
    # print(listtranspose(cases[0]))

    for i, case in enumerate(cases, start=1):
        status = None
        for player in ('X', 'O'):
            if straight(case, side=player):
                # print('%s won (straight)' % player)
                status = '%s won' % player
            if diagonal(case, side=player):
                # print('%s won (diagonal)' % player)
                status = '%s won' % player
            if straight(transpose(case), side=player):
                # print('%s won (straight, transposed)' % player)
                status = '%s won' % player
            if diagonal(transpose(case), side=player):
                # print('%s won (diagonal, transposed)' % player)
                status = '%s won' % player
        if status == None:
            # either draw or not completed
            if re.search(r'\.', case):
                status = 'Game has not completed'
            else:
                status = 'Draw'
        print('Case #%s: %s' % (i, status))

    # print(timeit.timeit("transpose('XXXT....OO......')", setup="from __main__ import transpose"))
    # print(timeit.timeit("slowtranspose('XXXT....OO......')", setup="from __main__ import slowtranspose"))
    # print(timeit.timeit("listtranspose('XXXT....OO......')", setup="from __main__ import listtranspose"))

if __name__ == '__main__':
    # main(filename='A-sample.in')
    main(filename='A-large.in')

