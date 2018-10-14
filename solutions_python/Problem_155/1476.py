#!/usr/bin/env python
from itertools import combinations
import sys


def problem(j, fi):
    n, seq = fi.readline().strip().split(' ')
    return n, int(seq[::-1])

def solve(params, problem_id):
    n, seq = params

    add = 0
    standing = 0
    level = 0
    next_level = 0

    while seq:
        at_level = seq % 10
        next_level += at_level
        seq = seq / 10

        if next_level == level:
            add += 1
            next_level += 1

        level += 1

    return add


if __name__ == '__main__':
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        total = int(fi.readline().strip())
        for i in range(1, total + 1):
            print "Processing case #{0}".format(i)
            res = solve(problem(i, fi), i)
            fo.write('Case #{0}: {1}\n'.format(i, res))
            fo.flush()
