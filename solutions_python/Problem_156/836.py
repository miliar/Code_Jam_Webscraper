#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem B. Infinite House of Pancakes
# https://code.google.com/codejam/contest/6224486/dashboard#s=p1
#

import sys
import random
import itertools


def solve(Plist):
    Plist.sort(reverse=True)
    minimum = P1 = Plist[0]
    if P1 > 3:
        for n in itertools.count(2):
            Pn = (P1 / n) if P1 % n == 0 else (P1 // n + 1)
            if Pn < 2:
                break
            # special
            check = 1 + solve(Plist[1:] + [Pn, P1 - Pn])
            if check < minimum:
                minimum = check
            else:
                break
    return minimum


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        D = IN.readline().strip()
        Plist = map(int, IN.readline().strip().split())
        OUT.write('Case #%d: %s\n' % (index + 1, solve(Plist)))


def makesample(T=100, Dmax=6, Pmax=9):
    print T
    for index in range(T):
        D = Dmax
        print D
        print ' '.join(str(random.randint(1, Pmax)) for n in range(D))


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)

