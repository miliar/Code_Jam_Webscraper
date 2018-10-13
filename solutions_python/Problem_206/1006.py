#!/usr/bin/pypy3
for T in range(int(input())):
    D, N = [int(i) for i in input().split()]
    h = [None]*N
    ext = lambda i : (h[i][0], h[i][1])
    for i in range(N):
        h[i] = [int(i) for i in input().split()]
    slowest = 1e6
    sval = 0
    scores = []
    for i in h:
        d = D - i[0]
        v = i[1]
        t = d/v
        scores.append(t)
    print("Case #{0}: {1:.6f}".format(T+1, D/max(scores)))

