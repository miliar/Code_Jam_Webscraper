#!/usr/bin/python3
import math
t = int(input())

for it in range(1, t+1) :
    N, P = [int(i) for i in input().split()]
    G0 = [int(i) for i in input().split()]
    G = [0]*(P+1)
    for g in G0: G[g%P] += 1
    ans = G[0]
    G[0] = 0
    if P == 4:
        g2 = G[2] // 2
        ans += g2
        G[2] -= g2 * 2
    for i in range(1, P):
        g = G[i]
        ii = P - i
        gg = G[ii]
        gi = g // 2 if ii == i else min(g, gg)
        ans += gi
        G[i] -= gi
        G[ii] -= gi
    m = 0
    while max(G) > 0:
        if m == 0: ans += 1
        g = -1
        for i in range(P):
            if G[i] == 0: continue
            g = i
            if i+m == P: break
        assert g > 0
        m = (m+g)%P
        G[g] -= 1
    print("Case #%d:"%it, ans)