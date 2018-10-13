# -*- coding: utf-8 -*-

import sys,math
fin = sys.stdin

T = int(fin.readline())

m = [0,1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011, \
    11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001, \
    1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111, \
    2000002,2001002,10000001,10011001,10100101,10111101,11000011,11011011,11100111, \
    11111111, 20000002]

m = [v*v for v in m]

def solve(A,B):
    from bisect import bisect_right, bisect_left
    aa = bisect_left(m, A)
    bb = bisect_right(m, B)
    return bb - aa

for case in xrange(1,T+1):
    A,B = map(long, fin.readline().split())
       
    print "Case #%d: %s" % (case, solve(A,B))