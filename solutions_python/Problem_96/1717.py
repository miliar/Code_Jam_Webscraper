import sys
from math import ceil

t = int(sys.stdin.readline())
for i in range(t):
    l = map(int, sys.stdin.readline().split())
    N = l[0]
    S = l[1]
    p = l[2]
    t = l[3:]
    count = 0
    for s in t:
        n = ceil(s / 3.)
        if n >= p:
            count += 1
        if n != 0 and n+1 == p and S > 0:
            S -= 1
            count += 1
    print "Case #%d: %d" % (i+1, count)


