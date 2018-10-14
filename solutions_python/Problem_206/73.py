# -*- coding: utf-8 -*-
T = int(raw_input())

for case in xrange(1, T + 1):
    D, N = map(int, raw_input().split()) 
    KS = [map(int, raw_input().split()) for i in xrange(N)]
    t = 0 
    for K, S in KS:
        if K >= D: continue
        tmp = 1.0*(D - K)/S
        t = max(t, tmp) 
    ans = D/t
    print "Case #%d: %.10f" % (case, ans)

