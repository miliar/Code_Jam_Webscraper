#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem A. Oversized Pancake Flipper
# https://code.google.com/codejam/contest/dashboard?c=3264486#s=p0
#

import sys
import random


def flip(S):
    return S.replace('-', '*').replace('+', '-').replace('*', '+')


def solve(S, K):
    count = 0
    while len(S) > K:
        if S[0] == '-':
            # flip
            count += 1
            S = flip(S[:K]) + S[K:]
        S = S[1:]

    if '-' not in S:
        # all '+'
        return count
    elif '+' not in S:
        # all '-' => flip
        return count + 1
    else:
        return 'IMPOSSIBLE'


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        S, K = IN.readline().split()
        OUT.write('Case #{}: {}\n'.format(index + 1, solve(S, int(K))))


def makesample(T=100, Slen=10):
    print(T)
    for index in range(T):
        S = ''.join(random.choice('+-') for n in range(Slen))
        K = random.randint(2, len(S))
        print('{} {}'.format(S, K))


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)
