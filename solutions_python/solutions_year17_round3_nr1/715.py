import sys
import math


def subSolve(c, k, first=False):
    c = sorted(c, key=lambda e: -e[0])
    assert len(c) >= k
    limit = len(c) - (k - 1)
    bestTotal = 0.0
    for i in range(1, limit+1):
        total = 0
        if first:
            choice = max(c[:i], key=lambda e: e[0]*e[0]+2*e[0]*e[1])
            r, h = choice
            total += math.pi * (r**2 + 2*r*h)
        else:
            choice = max(c[:i], key=lambda e: 2*e[0]*e[1])
            r, h = choice
            total += math.pi * (2*r*h)
        if k > 1:
            total += subSolve(c[i:], k-1)
        if total > bestTotal:
            bestTotal = total
    return bestTotal


def solve(line):
    tmp = line.split()
    n, k = int(tmp[0]), int(tmp[1])
    c = [(0.0, 0.0) for i in range(n)]
    for i in range(n):
        tmp = input().split()
        c[i] = (int(tmp[0]), int(tmp[1]))
    return subSolve(c, k, True)

n = int(input())

for i in range(n):
    solution = solve(input())
    print('Case #%d: %.9f' % (i+1, solution))
