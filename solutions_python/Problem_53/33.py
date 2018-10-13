#!/usr/bin/env python

T = int(raw_input())

for t in range(T):
    N, K = map(lambda x: int(x), raw_input().split())

    resp = 'OFF'
    if ((2**N)-1) == K%(2**N):
        resp = 'ON'
    print 'Case #%d: %s' % (t+1, resp)
