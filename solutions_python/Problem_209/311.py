#!/usr/bin/python3
from math import pi

def solve():
    n, k = list(map(int, input().split()))
    r, h, s = [0]*n, [0]*n, [0]*n
    for i in range(n):
        r[i], h[i] = list(map(int, input().split()))
        s[i] = 2*pi*r[i]*h[i]
    ss = sorted(s, reverse=True)
    results = [0]*n
    for i in range(n):
        results[i] = pi*r[i]*r[i]
        ts = 2*pi*r[i]*h[i]
        seen = False
        for j in range(k-1):
            results[i] += ss[j]
            if ss[j] == ts:
                seen = True
        results[i] += ts if not seen else ss[k-1]
    return max(results)

nn = int(input())
for t in range(nn):
    print('Case #{}: {}'.format(t+1, solve()))
