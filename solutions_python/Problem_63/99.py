#!/usr/bin/python

import math

def trials(P, L, C):
    r = math.ceil(math.log( float(L) / P ) / math.log(C))
    return math.ceil(math.log(r) / math.log(2))

cases = int(raw_input())
for case in range(1,cases+1):
    P, L, C = map(int, raw_input().split())
    answer = trials(P, L, C)
    print 'Case #%d: %d' % (case, answer)
