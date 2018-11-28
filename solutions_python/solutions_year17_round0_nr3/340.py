# -*- coding: utf-8 -*-
import heapq, sys

T = int(raw_input())
for case in xrange(1, T + 1):
    N, K = map(int, raw_input().split())
    mx, mn = N/2, (N - 1)/2
    x, y = 1, 1
    while x + y - 1 < K:
        if mx == mn:
            nx = x + y
            ny = x + y
        elif mx % 2:
            nx = 2*x + y
            ny = y
        else:
            nx = x
            ny = x + 2*y
        if 2*x + y > K:
            mx, mn = mx/2, max(0, (mx - 1)/2)
        elif 2*(x + y) > K:
            mx, mn = mn/2, max(0, (mn - 1)/2)
        else:
            mx, mn = mx/2, max(0, (mn - 1)/2)
        x, y = nx, ny
    print "Case #%s: %s %s" % (case, mx, mn)
