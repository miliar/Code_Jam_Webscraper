import sys
from itertools import cycle

T = int(sys.stdin.readline())

for Ti in xrange(T):
    R, k, N = map(int, sys.stdin.readline().split())
    gs = map(int, sys.stdin.readline().split())

    Rs = 0
    y = 0
    cur = 0
    on = 0

    for g in cycle(gs):
        if cur +g > k or on >= N:
            #print "- ", cur, on, Rs
            cur = 0
            on = 0
            Rs += 1
            if Rs >= R:
                print "Case #%d: %d" % (Ti+1, y)
                break
        #print g
        cur += g
        y += g
        on += 1
