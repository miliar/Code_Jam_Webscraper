#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem A. Mushroom Monster
# https://code.google.com/codejam/contest/4224486/dashboard#s=p0
#

import sys
import random


def method1(mlist):
    return sum(max(mlist[i] - m, 0) for i, m in enumerate(mlist[1:]))


def method2(mlist):
    rate = max(mlist[i] - m for i, m in enumerate(mlist[1:]))
    return sum((mlist[i] if mlist[i] < rate else rate) for i, m in enumerate(mlist[1:]))


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        IN.readline().strip()
        mlist = map(int, IN.readline().strip().split())
        y = method1(mlist)
        z = method2(mlist)
        OUT.write('Case #%d: %s %s\n' % (index + 1, y, z))


def makesample(Nmax=10, Mmax=100, T=100):
    print T
    for index in range(T):
        N = random.randint(2, Nmax)
        print N
        print ' '.join(str(random.randint(0, Mmax)) for n in range(N))


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)

