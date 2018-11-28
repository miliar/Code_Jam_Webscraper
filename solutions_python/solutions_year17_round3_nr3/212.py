#!/usr/bin/env python
# -*- Encoding: utf-8 -*-

from __future__ import print_function, unicode_literals

import heapq
from collections import defaultdict, deque

eps = 0.0000000000001


def solve(P, U, K):
    mn, mx = min(P), max(P)
    avg = sum(P) / len(P)

    while mn < mx and U > eps and avg < 1:
        want = [0 for i in range(len(P))]
        cnt = 0
        for i, p in enumerate(P):
            if p < avg:
                want[i] = (avg - p)
                if p + want[i] >= 1:
                    want[i] = 1 - p
                cnt += 1

        s = sum(want)
        if s == 0:
            break

        for i, w in enumerate(want):
            give = want[i] * (U / s)
            P[i] += give
            if P[i] > 1:
                give -= (P[i] - 1)
                P[i] = 1
            U -= give

        mn, mx = min(P), max(P)
        avg = sum(P) / len(P)

    assert U >= 0

    if U > 0:
        give = U / len(P)
        for i, p in enumerate(P):
            P[i] += give
            U -= give

    assert U <= eps or sum(P) / len(P) >= 1, "U = {}, {} / {} = {}".format(U, sum(P), len(P), sum(P) / len(P))

    mx = 1
    for p in P:
        mx *= p

    return mx


def solve2(P, U, K):
    while U > eps:
        mn = min(P)
        inds = [i for i, p in enumerate(P) if p == mn]
        other = [p for p in P if p > mn]
        if len(other) == 0:
            nxt = 1
        else:
            nxt = min(other)

        give = nxt - mn
        if give * len(inds) > U:
            give = U / len(inds)

        for i in inds:
            P[i] += give
        U -= give * len(inds)

    assert U >= -eps, U

    mx = 1
    for p in P:
        mx *= p

    return mx

if __name__ == '__main__':
    T = int(raw_input())
    for Ti in range(T):
        N, K = map(int, raw_input().strip().split(" "))
        U = float(raw_input())
        P = map(float, raw_input().strip().split(" "))

        ans = solve2(P, U, K)
        print("Case #{}: {:.6f}".format(Ti + 1, ans))
