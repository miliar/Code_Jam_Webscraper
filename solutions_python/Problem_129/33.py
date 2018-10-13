#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

import sys

from collections import defaultdict


def debug(*argv):
    print(*argv, file=sys.stderr)


def cost(on, off, c):
    dist = off - on
    return dist * c - (dist * (dist - 1) // 2)


fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    N, M = map(int, fin.readline().split())
    up = defaultdict(int)
    down = defaultdict(int)
    stations = set()
    expected_cost = 0
    for i in range(M):
        o, e, p = map(int, fin.readline().split())
        up[o] += p
        down[e] += p
        stations.add(e)
        stations.add(o)
        expected_cost += cost(o, e, N) * p

    stations = sorted(stations)

    real_cost = 0
    tickets = []
    prev_station = None
    for s in stations:
        u = up[s]
        d = down[s]
        # Number of tickets at each distance travelled
        tickets.append((s, u))

        while d > 0:
            station, number = tickets.pop()
            use = 0
            if number > d:
                number -= d
                use = d
                tickets.append((station, number))
            elif number == d:
                use = d
            else:
                use = number
            real_cost += cost(station, s, N) * use
            d -= use

    result = (expected_cost - real_cost) % 1000002013

    print("Case #%d: %s" % (case, result))

