# -*- coding: utf-8 -*-
import sys
import math
rl = lambda: sys.stdin.readline().strip()


T = int(rl())
for tcase in range(1, T + 1):
    N, K = map(int, rl().split())
    pies = [map(int, rl().split()) for i in range(N)]
    pies.sort(key=lambda x: x[0], reverse=True)
    dpdp = [[0 for i in range(N)] for j in range(K + 1)]
    for i in range(N):
        S = (pies[i][0] ** 2) * math.pi
        L = 2 * math.pi * pies[i][0] * pies[i][1]
        dpdp[0][i] = S + L
    for i in range(1, K):
        j = i - 1
        for k in range(N):
            L = 2 * math.pi * pies[k][0] * pies[k][1]
            best = L
            for l in range(k):
                if dpdp[j][l] + L > best:
                    best = dpdp[j][l] + L
            dpdp[i][k] = best
    best = 0
    for dp in dpdp:
        best = max(best, max(dp))
    print 'Case #%d: %f' % (tcase, best)
