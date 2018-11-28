#!/usr/bin/env python
# vim:fileencoding=utf-8

import sys
import pprint

from numpy import pi

pp = pprint.PrettyPrinter(indent=4)

ntest = 0
inputs = []


def solve():
    for t in range(ntest):
        N = inputs[t]["N"]
        K = inputs[t]["K"]
        cakes = inputs[t]["cakes"]

        cakes = sorted(cakes, reverse=True)
        # print(cakes)

        tops = []
        sides = []
        for i in range(N):
            cake = cakes[i]
            r, h = cake
            tops.append(pi * r ** 2)
            sides.append(2.0 * pi * r * h)

        # print(tops, sides)
        areas = []
        for i in range(N):
            sides_by_h = sorted(sides[i+1:],reverse=True)
            # print(i, "org", sides[i+1:])
            # print(i, "sorted", sides_by_h)
            # print(i, "sum", tops[i], sides[i], sides_by_h[i:i+K-1])
            areas.append(sum(sides_by_h[:K-1], tops[i] + sides[i]))

        # print("areas", areas)
        area = max(areas)

        print("Case #{0}: {1}".format(t + 1, area))


def parse():
    global ntest
    global inputs
    ntest = int(sys.stdin.readline().strip())
    for n in range(ntest):
        line = sys.stdin.readline().strip()
        N, K = line.split()
        N = int(N)
        K = int(K)
        mat_ary = []
        for n in range(N):
            row_ary = [int(c) for c in sys.stdin.readline().strip().split()]
            mat_ary.append(row_ary)

        inputs.append({"N": N, "K": K, "cakes": mat_ary})
    # pp.pprint(inputs)


if __name__ == '__main__':
    parse()
    solve()
