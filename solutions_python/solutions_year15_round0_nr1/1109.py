#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem A. Standing Ovation
# https://code.google.com/codejam/contest/6224486/dashboard#s=p0
#

import sys
import random


def solve(Slist):
    stand = 0
    need = 0
    for k, S in enumerate(map(int, Slist)):
        if stand < k:
            need += k - stand
            stand = k
        stand += S
    return need


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        Smax, Slist = IN.readline().strip().split()
        OUT.write('Case #%d: %s\n' % (index + 1, solve(Slist)))


def makesample(T=100, Smax=10):
    print T
    for index in range(T):
        S = random.randint(0, Smax)
        print S, ''.join(str(random.randint(0, 6) * random.randint(0, 6) // 10) for n in range(S)) + '1'


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)

