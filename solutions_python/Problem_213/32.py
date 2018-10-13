#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

import sys

from collections import defaultdict

def debug(*args):
    print(*args, file=sys.stderr)

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    N, C, M = map(int, fin.readline().split())
    # C: customers
    # N: seats
    # M: tickets
    number_on_seat = [0]*N
    total = [0]*C
    for i in range(M):
        p, b = map(int, fin.readline().split())
        p -= 1
        b -= 1
        number_on_seat[p] += 1
        total[b] += 1

    rides = max(total)
    promotions = 0
    while True:

        promotions = 0
        promotions_at_last = 0
        for seat in range(N-1, -1, -1):
            on_seat = number_on_seat[seat] + promotions_at_last
            to_promote = max(0, on_seat - rides)
            promotions += max(0, to_promote - promotions_at_last)
            promotions_at_last = to_promote

        if promotions_at_last == 0:
            break

        rides += 1


    print("Case #%d: %d %d" % (case, rides, promotions))

