#!/usr/bin/python3
from heapq import *
t = int(input())

for it in range(1, t+1) :
    N, Q = [int(i) for i in input().split()]
    mt = 0
    E, S = [], []
    D = []
    ans = []
    h = []
    for _ in range(N):
        e, s = [int(i) for i in input().split()]
        E.append(e)
        S.append(s)
    for _ in range(N):
        d = [int(i) for i in input().split()]
        D.append(d)
    for _ in range(Q):
        u, v = [int(i)-1 for i in input().split()]
        heappush(h, (0, u, 0, 0))
        bt = [10**11] * N
        while 1:
            t, c, e, s = heappop(h)
            #print(it,u,v,"=>",t,c,e,s)
            if c == v:
                ans.append(t)
                break
            if t < bt[c]:
                bt[c] = t
                heappush(h, (t, c, E[c], S[c]))
            for cc in range(N):
                if D[c][cc] < 0 or D[c][cc] > e: continue
                tt = t + D[c][cc] / s
                heappush(h, (tt, cc, e-D[c][cc], s))
    print("Case #%d:"%it, *ans)
