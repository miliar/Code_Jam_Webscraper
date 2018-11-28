#!/usr/bin/env python3
# coding=utf-8

"""
    Solve Round 1C 2017 p.A

    Author: killerrex
"""

import sys
import math


def read_int(fd):

    txt = fd.readline().split()

    return (int(s) for s in txt)


class Pancake:
    def __init__(self, r, h):
        super().__init__()
        self.r = r
        self.h = h
        self.lateral = 2*self.r*self.h
        self.base = self.r**2


class Stack:

    def __init__(self, fd):
        super().__init__()

        n, k = read_int(fd)
        self.k = k
        self._tower = []
        self._kitchen = []
        while len(self._kitchen) < n:
            r, h = read_int(fd)
            self._kitchen.append(Pancake(r, h))
        self._kitchen.sort(key=lambda pk: pk.r, reverse=True)

    def sort(self):
        self._tower.sort(key=lambda pk: pk.r, reverse=True)

    def area(self):
        self.sort()
        return self._tower[0].base + sum(pk.lateral for pk in self._tower)

    def essay(self, p: Pancake):
        if len(self._tower) < self.k:
            self._tower.append(p)
            return

        # From here we need them sorted
        self.sort()

        # First consideration: Replace the base
        old = self._tower[0].base + self._tower[0].lateral
        if len(self._tower) == 1 or p.r >= self._tower[1].r:
            new = p.base + p.lateral
        else:
            new = self._tower[1].base + p.lateral

        base_benefit = new - old

        if len(self._tower) == 1:
            tip_benefit = -1
            worst = None
        else:
            # No luck, try in the full stack
            worst = min(self._tower[1:], key=lambda pk: pk.lateral)
            tip_benefit = p.lateral - worst.lateral

        if base_benefit < 0 and tip_benefit < 0:
            return
        # At least one is positive...
        if base_benefit > tip_benefit:
            self._tower[0] = p
        else:
            # Replace it!
            j = self._tower.index(worst)
            self._tower[j] = p

    def optimum(self):
        for pk in self._kitchen:
            self.essay(pk)
        return self.area()

    def brute(self):
        return brute(self._kitchen, self.k)


def brute(kitchen, k):
    from itertools import combinations
    # Order the kitchen
    kitchen.sort(key=lambda pk: pk.r, reverse=True)
    best = 0
    for comb in combinations(kitchen, k):
        area = comb[0].base + sum(pk.lateral for pk in comb)
        best = max(best, area)
    return best


def solve(fd):
    total, = read_int(fd)

    for j in range(total):
        # Read next problem
        stack = Stack(fd)
        # Give results in mm²
        area = stack.optimum() * math.pi
#        best = stack.brute() * math.pi
#        if best > area:
#            raise ValueError
        print("Case #{}: {:.9f}".format(j+1, area))


def start():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as fd:
            solve(fd)
    else:
        solve(sys.stdin)


if __name__ == '__main__':
    start()
