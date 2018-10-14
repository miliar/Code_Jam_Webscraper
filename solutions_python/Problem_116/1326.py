#!/usr/bin/python

import sys

def solve(puzzle):
    lines = list(puzzle)
    lines.extend(zip(*puzzle))
    lines.append([puzzle[i][i] for i in range(4)])
    lines.append([puzzle[3-i][i] for i in range(4)])

    winner = filter(None, [getWinner(line) for line in lines])
    if len(winner):
        return winner[0] + ' won'

    if any('.' in line for line in lines):
        return 'Game has not completed'

    return 'Draw'

def getWinner(line):
    if not 'X' in line and not '.' in line:
        return 'O'
    if not 'O' in line and not '.' in line:
        return 'X'
    return None

input = [line.strip() for line in sys.stdin]

for index in range(int(input[0])):
    startIndex = index * 5 + 1
    print 'Case #%d: %s' % (index + 1, solve(input[startIndex:startIndex + 4]))
