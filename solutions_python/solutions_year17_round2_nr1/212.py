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
    D, N = map(int, input().split(" "))
    K = [None] * N
    S = [None] * N
    for i in range(N):
        K[i], S[i] = map(int, input().split(" "))

    g = [None] * N
    for i in range(N):
        g[i] = (D - K[i]) / S[i]
    return D / max(g)


def main():
    n_cases = int(input())
    for i in range(n_cases):
        print("Case #{}: {}".format(i + 1, solve()))


if __name__ == "__main__":
    main()
