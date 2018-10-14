#!/usr/bin/env python

from sys import argv
from os.path import basename, splitext
from logging import basicConfig, DEBUG, INFO, debug

from math import log10, ceil

def is_palindrome(x):
    return str(x) == str(x)[::-1]


def solve(t, A, B):
    debug(A)
    debug(B)
    p = range(1, 10, 1) + [10*i+i for i in range(1, 10, 1)] + [101]

    pi = 0
    go = True
    result = 0
    while True:
        p2 = p[pi]*p[pi]
        pi += 1
        if A <= p2 and p2 <= B and is_palindrome(p2):
            result += 1
        if p2 > B:
            break
        if pi == len(p) - 1:
            for i in range(1, 10, 1):
                # next = i*pow(10, ceil( log10(x + 1) ) + 1) + 10*x + i
                next = str(i) + str(x) + str(i)
                p.append(int(next))
    debug(p)
    return 'Case #{0}: '.format(t + 1) + str(result) + '\n'


if "__main__" == __name__:
    level=INFO
    if 0:
        level=DEBUG
    basicConfig(format='%(levelname)s: %(message)s', level=level)
    infname = argv[1]
    oufname = splitext(basename(infname))[0] + '.out'
    with open(infname, 'r') as inf:
        with open(oufname, 'w') as ouf:
            t = int(inf.readline())
            for i in range(t):
                (A, B) = (int(x) for x in inf.readline().strip().split(' '))
                ouf.write(solve(i, A, B))
