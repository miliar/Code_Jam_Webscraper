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
    Ac, Aj = map(int, input().split(" "))
    C = [None] * Ac
    D = [None] * Ac
    J = [None] * Aj
    K = [None] * Aj
    for i in range(Ac):
        C[i], D[i] = map(int, input().split(" "))
    for i in range(Aj):
        J[i], K[i] = map(int, input().split(" "))

    # small(Ac+Aj <= 2)
    if Ac == 1 or Aj == 1:
        return 2
    if Ac == 2 and Aj == 0:
        S = C
        E = D
    elif Aj == 2 and Ac == 0:
        S = J
        E = K
    else:
        return 0
    durations = [E[0] - S[1], E[1] - S[0]]
    durations = map(lambda t: t if t > 0 else 1440 + t, durations)
    if min(durations) <= 720:
        return 2
    return 4


def main():
    n_cases = int(input())
    for i in range(n_cases):
        print("Case #{}: {}".format(i + 1, solve()))


if __name__ == "__main__":
    main()
