#!/usr/bin/python

for i in range(1, int(raw_input())+1):
    N, K = map(int, raw_input().split())
    result = 'ON'
    for j in range(N):
        if K & (1<<j) == 0:
            result = 'OFF'
            break
    print 'Case #%d: %s' % (i, result)
