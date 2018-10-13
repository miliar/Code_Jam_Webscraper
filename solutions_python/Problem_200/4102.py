#!/usr/bin/env python3

import sys
import math
import heapq
import itertools
import bisect
import traceback
from array import array
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from collections import namedtuple

sys.setrecursionlimit(10000)

#constants
INF = float('inf')
EPS = 1e-10
PI = math.pi


def carry(S, i):
    #print(S)
    p = i-1
    tmps = S[:i][::-1]
    #print('tmps', tmps)
    for j in range(len(tmps)):
        if i==j+1:
            break
        if tmps[j+1] < tmps[j]:
            p = j
    #print('point in tmps', p)
    p = i-1-p
    #print('point in S', p)

    #print('S[p]', S[p])
    S = S[:p] + str(int(S[p])-1) + S[p+1:]
    #print('After change', S)
    #print()
    for j in range(len(S[p+1:])):
        S = S[:p+1+j] + '9' + S[p+1+j+1:]

    return S


def solve(S):
    carry_flag = False
    for i in range(len(S)):
        if i == 0:
            continue
        if S[i-1] > S[i]:
            if not carry_flag:
                S = carry(S, i)
                carry_flag = True
            S = S[:i] + '9' + S[i+1:]

    while S[0] == '0':
        S = S[1:]
    return S


def main():
    T = int(input())
    for i in range(T):
        S = input()
        ans = solve(S)
        print("Case #{0}: {1}".format(i+1, ans))
    return


if __name__ == '__main__':
    main()

