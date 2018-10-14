# coding: utf-8


import sys
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
    N, P = map(int, input().split(" "))
    R = list(map(int, input().split(" ")))
    Q = [None] * N
    for i in range(N):
        Q[i] = list(map(int, input().split()))
        Q[i].sort()
    idx = [0] * N
    valid_packs = 0
    while P not in idx:
        pack = [Q[i][idx[i]] for i in range(N)]
        c_lowers = [pack[i] / (1.1 * R[i]) for i in range(N)]
        c_uppers = [pack[i] / (0.9 * R[i]) for i in range(N)]
        c_lowers_int = map(math.ceil, c_lowers)
        c_uppers_int = map(math.floor, c_uppers)
        if max(c_lowers_int) <= min(c_uppers_int):
            valid_packs += 1
            for i in range(N):
                idx[i] += 1
        else:
            idx[c_lowers.index(min(c_lowers))] += 1
    return valid_packs


def main():
    n_cases = int(input())
    for i in range(n_cases):
        print("Case #{}: {}".format(i + 1, solve()))


if __name__ == "__main__":
    main()
