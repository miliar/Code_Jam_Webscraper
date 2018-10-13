#!/usr/bin/env python3
# coding=utf-8

"""
    Solve Quals 2017 p.A

    Author: killerrex
"""

import sys


def flipflop(pancakes, k):

    flips = 0
    n = 0
    while n < len(pancakes):
        if not pancakes[n]:
            # A minus... invert the next k
            try:
                for i in range(k):
                    pancakes[n+i] = not pancakes[n+i]
            except IndexError:
                return 'IMPOSSIBLE'
            flips += 1
        n += 1
    return flips


def solve(fd):
    total = int(fd.readline().strip())

    for j in range(total):
        raw, k = fd.readline().split()
        k = int(k)
        pancakes = [c == '+' for c in raw]

        print("Case #{}: {}".format(j+1, flipflop(pancakes, k)))


def start():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as fd:
            solve(fd)
    else:
        solve(sys.stdin)


if __name__ == '__main__':
    start()