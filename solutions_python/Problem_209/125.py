#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from array import *
import bisect
import math
# from collections import *
# from fractions import *
# from heapq import *
# from itertools import *
# from math import *
# from re import *
# from string import *

def solve():
    N, K = map(int, input().split())
    r_and_hs = []
    for n in range(N):
        r, h = map(int, input().split())
        r_and_hs.append((r,h))
    r_and_hs.sort()

    ans = 0.0
    scores = []
    for i in range(N):
        r, h = r_and_hs[i]
        bottom_score = 2.0 * math.pi * r * h
        if len(scores) >= K - 1:
            local_ans = -sum(scores[:K-1])
            local_ans += math.pi * (r ** 2) + bottom_score
            ans = max(ans, local_ans)
        bisect.insort_left(scores, -bottom_score)
    print("{:.15f}".format(ans))

T = int(input())
for testcase in range(T):
    print("Case #{}: ".format(testcase+1), end="")
    solve()

