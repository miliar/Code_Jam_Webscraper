#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem A. The Repeater
# https://code.google.com/codejam/contest/2994486/dashboard#s=p0
#

import sys


def solve(strings):
    strings = [list(s) for s in strings]
    chars = []
    for c in strings[0]:
        if not chars or c != chars[-1]:
            chars.append(c)

    total = 0
    for c in chars:
        counts = []
        for s in strings:
            if not s or s[0] != c:
                return 'Fegla Won'
            count = 0
            while s and s[0] == c:
                s.pop(0)
                count += 1
            counts.append(count)

        # try 1
        goal = sum(counts) // len(counts)
        total += min(sum(abs(goal - c) for c in counts),
                     sum(abs(goal + 1 - c) for c in counts))

    for s in strings:
        if s:
            return 'Fegla Won'
    return total


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        N = int(IN.readline())
        strings = [IN.readline().strip() for n in range(N)]
        OUT.write('Case #%d: %s\n' % (index + 1, solve(strings)))


def makesample(Nmax=100, T=100):
    import random

    print T
    for index in range(T):
        print


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)

