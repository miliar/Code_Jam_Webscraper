#/usr/bin/env python2.7

"""Tic-Tac-Toe-Tomek"""

"""
Output:

X won
O won
Draw
Game has not completed
"""

import sys


def decide(lines):
    full = True
    for row in lines:
        s = set(row)
        if '.' in s:
            full = False
        else:
            s.discard('T')
            if len(s) == 1:
                return '{} won'.format(s.pop())

    for col in [[lines[row][col] for row in range(4)] for col in range(4)]:
        s = set(col)
        s.discard('T')
        if len(s) == 1 and '.' not in s:
            return '{} won'.format(s.pop())

    s = set(lines[i][i] for i in range(4))
    s.discard('T')
    if len(s) == 1 and '.' not in s:
        return '{} won'.format(s.pop())

    s = set(lines[i][3-i] for i in range(4))
    s.discard('T')
    if len(s) == 1 and '.' not in s:
        return '{} won'.format(s.pop())

    if not full:
        return 'Game has not completed'
    return 'Draw'


def run(infile):
    f = open(infile)
    num = int(f.readline())
    for i in xrange(num):
        lines = []
        for j in range(4):
            lines.append(f.readline().strip())
        assert f.readline().strip() == ''
        print 'Case #{count}: {}'.format(decide(lines), count=i+1)


if __name__ == '__main__':
    run(sys.argv[1])
