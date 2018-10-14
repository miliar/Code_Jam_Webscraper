#!/usr/bin/python

import sys

def N(): return tuple(map(int, sys.stdin.readline().split()))

T = N()[0]
for t in range(1, T + 1):
    p1 = N()[0]
    r1 = [set(N()) for i in range(4)][p1-1]
    p2 = N()[0]
    r2 = [set(N()) for i in range(4)][p2-1]
    rs = r1 & r2
    if len(rs) == 1:
        answer = str(rs.pop())
    elif len(rs) == 0:
        answer = "Volunteer cheated!"
    else:
        answer = "Bad magician!"
    print "Case #%d: %s" % (t, answer)

