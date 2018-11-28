
from __future__ import division
for T in range(1, int(raw_input())+1):
    D, N = map(int,raw_input().split())
    M = 0
    for i in xrange(N):
        A, B = map(int, raw_input().split())
        C = (D-A)/B
        if C > M: M = C
    print "Case #%d: %.6f"%(T, D/M)