#!/usr/bin/env python
import sys


def ilog2(x):
    return x.bit_length() - 1


def solve(N, K):
    lvl = ilog2(K)
    lvl_cap = (1 << lvl)
    pool = N - K + 1
    cell = (pool + lvl_cap - 1) / lvl_cap
    return cell / 2, (cell - 1) / 2


if __name__ == '__main__':
    sys.stdin.readline()
    for num, line in enumerate(sys.stdin, 1):
        N, K = map(int, line.split())
        y1, y2 = solve(N, K)
        print "Case #{0}: {1} {2}".format(num, y1, y2)
