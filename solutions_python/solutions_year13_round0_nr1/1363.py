# coding: utf-8

import sys

def test(seq):
    seq = list(seq)
    if seq.count('X') + seq.count('T') == 4:
        return 'X won'
    if seq.count('O') + seq.count('T') == 4:
        return 'O won'

def solve(lines):
    # horizontal test
    for line in lines:
        a = test(line)
        if a:
            return a

    # vertical test
    for line in zip(*lines):
        a = test(line)
        if a:
            return a

    # diagonal test
    a = test(lines[i][i] for i in range(4))
    if a:
        return a

    a = test(lines[i][4-i-1] for i in range(4))
    if a:
        return a

    if sum(line.count('.') for line in lines):
        return 'Game has not completed'

    return 'Draw'

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        lines = list(reversed(f.read().split('\n')))
        T = int(lines.pop())
        for t in range(T):
            result = solve([lines.pop() for i in range(4)])
            lines.pop() # for an empty line
            print 'Case #{}: {}'.format(t + 1, result)
