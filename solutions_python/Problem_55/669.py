#!/usr/bin/env python3
def solve(R, k, g):
    euros = 0
    for i in range(R):
        s = 0
        for i, x in enumerate(g):
            if s + x > k:
                break
            s += x
        euros += s
        g = g[i:] + g[:i]
    return euros
    
T = int(input())
for case in range(1, T + 1):
    R, k, N = [int(w) for w in input().split()]
    g = [int(w) for w in input().split()]
    print("Case #{0}: {1}".format(case, solve(R, k, g)))
