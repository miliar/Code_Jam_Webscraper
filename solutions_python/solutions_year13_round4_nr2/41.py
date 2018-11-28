#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

import sys


def debug(*argv):
    print(*argv, file=sys.stderr)


def best_position(k, n):
    """
    1-based indexing
    """
    total = 2 ** n
    above = k - 1
    below = total - k
    wins = 0
    while below > 0:
        wins += 1
        killed_above = above // 2
        killed_below = (above + below + 1) // 2 - killed_above
        above -= killed_above
        below -= killed_below
    losses = n - wins
    position = 2 ** losses
    return position


def worst_position(k, n):
    total = 2 ** n
    above = k - 1
    below = total - k
    losses = 0
    while above > 0:
        losses += 1
        killed_below = below // 2
        killed_above = (above + below + 1) // 2 - killed_below
        above -= killed_above
        below -= killed_below

    wins = n - losses
    position = total - 2 ** wins + 1
    return position


# n = 6
# for i in range(1, 2**n+1):
#     best = best_position(i, n)
#     worst = worst_position(i, n)
#     debug(i, best, worst)



fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    N, P = map(int, fin.readline().split())

    g = 0

    T = 2 ** N
    p = T
    l = 1
    for i in range(N+1):
        v = T - 2 ** (N - i)
        limit = (2 ** i)
        if P >= limit:
            l = v


        v = 2 ** (i+1) - 1
        if i == N:
            v = T
        limit = T - 2 ** (N - i)
        #debug(i, v, limit)
        if P > limit:
            g = v-1




    #debug('-')
    # g = 0
    # l = 0
    # for i in range(1, 2 ** N + 1):
    #     best = best_position(i, N)
    #     worst = worst_position(i, N)
    #     if best <= P:
    #         l = i
    #     if worst <= P:
    #         g = i
    print("Case #%d: %d %d" % (case, g, l))


# Case #1: 0 0
# Case #2: 0 4
# Case #3: 0 4
# Case #4: 0 6
# Case #5: 2 6
# Case #6: 2 6
# Case #7: 6 6
# Case #8: 7 7
# 1 1 1
# 2 2 5
# 3 2 5
# 4 2 7
# 5 2 7
# 6 4 7
# 7 4 7
# 8 8 8

