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


def solve(S, K):
    C=0
    for i in range(len(S)-K+1):
        if S[i] == '-':
            C+=1
            for j in range(K):
                if S[i+j] == '-':
                    S = S[:i+j] + '+' + S[i+j+1:]
                else:
                    S = S[:i+j] + '-' + S[i+j+1:]
    if '-' in S:
        C = "IMPOSSIBLE"
    return C


def main():
    T = int(input())
    for i in range(T):
        S, K = input().split()
        ans = solve(S, int(K))
        print("Case #{0}: {1}".format(i+1, ans))
    return


if __name__ == '__main__':
    main()

