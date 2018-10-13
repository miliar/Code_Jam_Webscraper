#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem B. Tidy Numbers
# https://code.google.com/codejam/contest/dashboard?c=3264486#s=p1
#

import sys
import random


def solve(N):
    n = str(N)
    if ''.join(sorted(list(n))) == n:
        return N

    answer = int(n[0])
    n = n[1:]
    while n:
        if int(n[0]) < answer % 10:
            return solve((answer - 1) * 10 ** len(n) + 10 ** len(n) - 1)
        answer = answer * 10 + int(n[0])
        n = n[1:]
    return answer


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        N = int(IN.readline())
        OUT.write('Case #{}: {}\n'.format(index + 1, solve(N)))


def makesample(T=100, Nmax=10 ** 18):
    print(T)
    for index in range(T):
        N = random.randint(1, Nmax)
        print(N)


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)
