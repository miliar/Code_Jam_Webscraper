#!/usr/bin/python3
import math
t = int(input())

for it in range(1, t+1) :
    N, K = [int(i) for i in input().split()]
    R, H = [], []
    P = []
    for _ in range(N):
        r, h = [int(i) for i in input().split()]
        h *= r*2
        r *= r
        R.append(r)
        H.append(h)
        P.append((h, r))
    P = sorted(P, key = lambda s: -s[0])
    mr = 0
    ans0 = 0
    for k in range(K-1):
        ans0 += P[k][0]
        mr = max(mr, P[k][1])
    ans = 0
    for k in range(K-1, N):
        ar = max(mr, P[k][1]) + P[k][0]
        ans = max(ans, ans0 + ar)
    print("Case #%d:"%it, math.pi * ans)