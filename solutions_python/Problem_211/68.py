#!/usr/bin/python3

import sys
from math import pi

def mul(l):
    ans = 1.0
    for x in l:
        ans *= x
    return ans

def eq(a, b):
    return abs(a - b) < 1e-10

def solve_easy(n, u, p):
    # print(u)
    p.sort()  # 0 ... n - 1
    # print(p)
    best = 0.0
    for i in range(n):
        # Give to 0 ... i
        each = (sum(p[:i+1]) + u) / (i + 1)
        if each > 1.0:
            continue
        if i > 0 and (each <= max(p[:i+1]) and not eq(each, max(p[:i+1]))):
            continue  # Not possible
        # print([each] * (i + 1) + p[i+1:])
        ans = each**(i + 1) * mul(p[i+1:]) 
        best = max(ans, best)
    return best
    
n_cases = int(sys.stdin.readline())

for i in range(1, n_cases+1):
    n, k = map(int, sys.stdin.readline().split())
    u = float(sys.stdin.readline())
    p = [float(x) for x in sys.stdin.readline().split()]
    ans = solve_easy(n, u, p)
    print('Case #{0}: {1}'.format(i, ans))
