from __future__ import print_function

def get_min_minutes(p, memo):
    p = sorted(p)
    if tuple(p) in memo:
        return memo[tuple(p)]

    mi = p[-1]
    if p[-1] > 3:
        for take in range(2, (p[-1]//2)+1):
            v = get_min_minutes(p[:-1] + [take, p[-1] - take], memo) + 1
            mi = min(v, mi)

    memo[tuple(p)] = mi
    return mi

import sys

fin = sys.stdin

num_cases = int(fin.readline().strip())

for C in range(num_cases):
    D = int(fin.readline().strip())
    p = [int(x) for x in fin.readline().split()]
    memo = {}
    print("Case #{}: {}".format(C+1, get_min_minutes(sorted(p), memo)))