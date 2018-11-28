import math
import sys
sys.setrecursionlimit(1000000)
p = None


def hh(p):
    return 2 * math.pi * p[0] * p[1]


def ss(p):
    return math.pi * p[0] * p[0]

dp = {}


def rec(prev, k):
    if (prev, k) in dp:
        return dp[(prev, k)]
    if k == 0:
        return 0
    res = 0
    for i in range(prev + 1, len(p)-k+1):
        s = ss(p[i]) + hh(p[i])
        if prev >= 0:
            s -= ss(p[prev])
        res = max(res, s + rec(i, k-1))
    return res


tests = int(raw_input())
for test in range(tests):
    n, k = map(int, raw_input().split())
    p = [map(int, raw_input().split()) for _ in range(n)]
    p.sort()
    dp = {}
    print "Case #{}: {}".format(test+1, rec(-1, k))

