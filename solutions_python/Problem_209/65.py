#!/usr/bin/python3

import sys
from math import pi

def h_area(p):
    r = p[0]
    h = p[1]
    return h * 2 * pi * r

def p_area(p):
    r = p[0]
    h = p[1]
    return pi * r**2

def solve(n, k, l):
    l.sort(reverse=True)
    # print(l)
    best = {(i, 0): 0 for i in range(n + 1)}
    for i in range(1, k + 1):
        best[(0, i)] = float('-inf')
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            best[(j, i)] = max(best[(j - 1, i)], best[(j - 1, i - 1)] + h_area(l[j - 1]) + (p_area(l[j - 1]) if i == 1 else 0))
    return best[(n, k)]        

n_cases = int(sys.stdin.readline())

for i in range(1, n_cases+1):
    n, k = map(int, sys.stdin.readline().split())
    pancakes = []
    for j in range(1, n+1):
        r, h = map(int, sys.stdin.readline().split())
        pancakes.append((r, h))
    max_exposed = solve(n, k, pancakes)
    print('Case #{0}: {1}'.format(i, max_exposed))
