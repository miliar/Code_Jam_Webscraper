#!/bin/python
from math import pi
from collections import defaultdict

def side(pancake):
    return 2.0 * pi * pancake[0] * pancake[1]

def area(pancake):
    return pi * pancake[0] * pancake[0]

for test in range(int(input())):
    n, k = map(int, input().split())

    pancakes = []
    for i in range(n):
        r, h = map(int, input().split())
        pancakes.append((r, h))

    pancakes = sorted(pancakes, key = lambda pancake: (pancake[0], pancake[1]))
    # for i, pancake in enumerate(pancakes):
    #     print("Pancake %i: side=%.2f, area=%.2f" % (i, side(pancakes[i]), area(pancakes[i])))

    dp = defaultdict(float)
    # dp[i][j][0/1] = maximum obtainable exposed surface
    #                 using j of the first i pancakes
    #                 having added (or not) the base surface

    for i in range(0, n):
        # dp[(i, 1, 0)] = side(pancakes[i])
        # dp[(i, 1, 1)] = side(pancakes[i]) + area(pancakes[i])
        for j in range(0, k+1):
            dp[(i, j, 0)] = dp[(i-1, j, 0)]
            dp[(i, j, 1)] = dp[(i-1, j, 1)]

        for j in range(0, k):
            # i want to use pancake i as a base
            # i already have j pancakes

            dp[(i, j+1, 1)] = max(dp[(i, j+1, 1)], dp[(i-1, j, 0)] + area(pancakes[i]) + side(pancakes[i]))
            dp[(i, j+1, 0)] = max(dp[(i, j+1, 0)], dp[(i-1, j, 0)] + side(pancakes[i]))

    # sol = max([dp[(i, k, 1)] for i in range(n)])
    sol = dp[(n-1, k, 1)]
    print("Case #%i: %.9f" % (1+test, sol))
