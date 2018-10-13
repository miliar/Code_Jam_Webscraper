# coding: utf-8

import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect


def array2d(d1, d2, init=None):
    return [[init for _ in range(d2)] for _ in range(d1)]


def solve_small():
    N, Q = map(int, input().split(" "))
    E = [None] * N
    S = [None] * N
    for i in range(N):
        E[i], S[i] = map(int, input().split(" "))
    dist_mat = [None] * N
    for i in range(N):
        dist_mat[i] = list(map(int, input().split(" ")))
    uvs = [None] * N
    for i in range(Q):
        uvs[i] = tuple(map(int, input().split(" ")))

    # small
    # dist[i]: dist between town i to i+1
    # no route between town N-1 to 0
    dist = [None] * (N-1)
    for i in range(N-1):
        dist[i] = dist_mat[i][i+1]

    # u=1, v=N
    total_times = [None] * N
    total_times[0] = 0
    for i in range(1, N):
        tmp_t = []
        for j in range(0, i):
            d = sum(dist[j:i])
            if E[j] < d:
                continue
            t = total_times[j] + d / S[j]
            tmp_t.append(t)
        total_times[i] = min(tmp_t)

    return total_times[N-1]


def main():
    n_cases = int(input())
    for i in range(n_cases):
        print("Case #{}: {}".format(i + 1, solve_small()))


if __name__ == "__main__":
    main()
