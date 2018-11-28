#!/usr/bin/env python3

def solve(d, n, ks):
    return (d / max((d - k) / s for k, s in ks))

for N in range(int(input())):
    d, n = [int(x) for x in input().split()]
    ks = [[int(x) for x in input().split()] for _ in range(n)]
    print('Case #{}: {}'.format(N + 1, solve(d, n, ks)))
