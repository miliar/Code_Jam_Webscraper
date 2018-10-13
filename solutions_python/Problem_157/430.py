#!/usr/bin/env python

from __future__ import division, print_function

import fileinput


table = {}

table['e'] = {
    'e': (True, 'e'), 'i': (True, 'i'), 'j': (True, 'j'), 'k': (True, 'k')
}

table['i'] = {
    'e': (True, 'i'), 'i': (False, 'e'), 'j': (True, 'k'), 'k': (False, 'j')
}

table['j'] = {
    'e': (True, 'j'), 'i': (False, 'k'), 'j': (False, 'e'), 'k': (True, 'i')
}

table['k'] = {
    'e': (True, 'k'), 'i': (True, 'j'), 'j': (False, 'i'), 'k': (False, 'e')
}


def evaluate(positive, value, expr):
    for symbol in expr:
        sign, value = table[value][symbol]
        positive = not (positive ^ sign)
    return positive, value


def partition(expr):
    positive, value = evaluate(True, 'e', expr)
    if positive or value != 'e':
        return 'NO'
    i, si = 'e', True
    for p1 in range(len(expr)-2):
        si, i = evaluate(si, i, expr[p1])
        j, sj = 'e', True
        for p2 in range(p1+1, len(expr)-1):
            sj, j = evaluate(sj, j, expr[p2])
            if si and sj and i == 'i' and j == 'j':
                return 'YES'
    return 'NO'


if __name__ == '__main__':
    for i, line in enumerate(fileinput.input()):
        if i == 0:
            continue
        elif i % 2 == 1:
            _, repeat = map(int, line.strip().split())
        else:
            i //= 2
            print("Case #{}: {}".format(i, partition(line.strip()*repeat)))
