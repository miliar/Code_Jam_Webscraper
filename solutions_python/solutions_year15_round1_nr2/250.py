#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem B. Haircut
# https://code.google.com/codejam/contest/4224486/dashboard#s=p1
#

import sys
import random


def gcd(x, y):
    return gcd(y, x % y) if y else x


def lcm(x, y):
    return x * y / gcd(x, y)


class Barbar:
    def __init__(self, i, m):
        self.index = i
        self.minute = m
        self.next = 0

    def __cmp__(self, other):
        return cmp(self.next, other.next) or cmp(self.index, other.index)

    def __repr__(self):
        return '[%d]%d' % (self.index, self.next)

    def start(self):
        past = self.next
        self.next = self.minute
        return past

    def past(self, minute):
        self.next -= minute


def solve(Mlist, N):
    loop = reduce(lambda x, y: lcm(x, y), Mlist, 1)
    loopcnt = sum(loop / m for m in Mlist)
    N = (N - 1) % loopcnt

    mlist = sorted(Barbar(i + 1, m) for i, m in enumerate(Mlist))

    for n in range(N):
        m = mlist[0].start()
        map(lambda x: x.past(m), mlist[1:])
        mlist.sort()
    return mlist[0].index


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        B, N = map(int, IN.readline().strip().split())
        Mlist = map(int, IN.readline().strip().split())
        OUT.write('Case #%d: %s\n' % (index + 1, solve(Mlist, N)))


def makesample(Bmax=5, Mmax=25, T=100, Nmax=10 ** 9):
    print T
    for index in range(T):
        B = random.randint(1, Bmax)
        print B, random.randint(1, Nmax)
        print ' '.join(str(random.randint(1, Mmax)) for k in range(B))


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)

