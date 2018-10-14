#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem B. Manage your Energy
# https://code.google.com/codejam/contest/2418487/dashboard#s=p1
#

import sys
import itertools


def step(Emax, R, vlist, E):
    v, vlist = vlist[0], vlist[1:]
    if not vlist:
        # left all energy
        return E * v
    return max(e * v + step(Emax, R, vlist, min(E - e + R, Emax)) for e in range(0, E+1))


def solve(E, R, vlist):
    return step(E, R, vlist, E)


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        E, R, N = map(int, IN.readline().split())
        vlist = map(int, IN.readline().split())
        OUT.write('Case #%d: %d\n' % (index + 1, solve(E, R, vlist)))


def makesample(Emax=5, Rmax=5, Nmax=10, vmax=10, T=100):
    import random
    print T
    for index in range(T):
        E = random.randint(1, Emax)
        R = random.randint(1, Rmax)
        N = random.randint(1, Nmax)
        vlist = [random.randint(1, vmax) for n in range(N)]
        print E, R, N
        print ' '.join(map(str, vlist))


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)

