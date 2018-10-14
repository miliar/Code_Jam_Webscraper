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


def solve():
    N, K = map(int, input().split(" "))
    R = [None] * N
    H = [None] * N
    for i in range(N):
        R[i], H[i] = map(int, input().split(" "))

    # # small
    # max_s = 0
    # for c in itertools.combinations(range(N), K):
    #     rs = [R[i] for i in c]
    #     hs = [H[i] for i in c]
    #     s = max(rs)**2 + 2 * sum([r * h for r, h in zip(rs, hs)])
    #     if s > max_s:
    #         max_s = s

    # large
    rh2 = [2 * r * h for r, h in zip(R, H)]
    id_rh2 = {i: rh2[i] for i in range(N)}
    ids_top_rh2 = sorted(id_rh2.keys(), key=lambda i: -id_rh2[i])[0:K]
    max_r = max([R[i] for i in ids_top_rh2])
    min_rh = rh2[ids_top_rh2[-1]]

    max_d = 0
    max_i = ids_top_rh2[-1]
    for i in range(N):
        if i in ids_top_rh2:
            continue
        if R[i] < max_r:
            continue
        d = R[i]**2 + rh2[i] - max_r**2 - min_rh
        if d > max_d:
            max_d = d
            max_i = i

    ids_top_rh2[-1] = max_i
    max_r = max([R[i] for i in ids_top_rh2])
    s = max_r**2 + sum([rh2[i] for i in ids_top_rh2])

    return s * math.pi


def main():
    n_cases = int(input())
    for i in range(n_cases):
        print("Case #{}: {}".format(i + 1, solve()))


if __name__ == "__main__":
    main()
