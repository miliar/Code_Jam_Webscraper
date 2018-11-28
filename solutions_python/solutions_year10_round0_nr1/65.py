#!/bin/python

import sys

inf = sys.stdin
T = int(inf.readline())
    
for t in range(T):
    n, k = map(int, inf.readline().split())
    result = 'ON'
    # if last n bits of k are set then 'ON'
    for i in range(n):
        if not k & 0x01:
            result = 'OFF'
            break
        k >>= 1
    print 'Case #%d: %s' % (t+1, result)