import sys
import itertools
import math
import collections
import functools

sys.setrecursionlimit(1000)

T = int(raw_input())
for testId in range(T):
    N, X = map(int, raw_input().split())
    V = sorted(map(int, raw_input().split()))
    done = [False] * N

    res = 0
    i = N-1
    while i >= 0:
        if not done[i]:
            done[i] = True
            res += 1
            for j in range(i-1, -1, -1):
                if done[j]:
                    continue
                if V[i] + V[j] <= X:
                    done[j] = True
                    break
        i -= 1

    print "Case #{:d}: {:d}".format(testId+1, res)
