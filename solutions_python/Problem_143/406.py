#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem *. 
# https://code.google.com/codejam/contest/***
#

import sys


def solve(A, B, K):
    return sum(1 for a in range(A) for b in range(B) if a & b < K)


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        A, B, K = map(int, IN.readline().split())
        OUT.write('Case #%d: %d\n' % (index + 1, solve(A, B, K)))


def makesample(MAX=1000, T=100):
    import random

    print T
    for index in range(T):
        A = random.randint(1, MAX)
        B = random.randint(1, MAX)
        K = random.randint(1, MAX)
        print A, B, K


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)

