import sys
import math

t = int(sys.stdin.readline())
for e in xrange(1, t+1):
    c, f, x = map(float, sys.stdin.readline().split())
    income = 2.0
    best = 10**88
    curtime = 0.0
    while True:
        tm = curtime + x / income
        if tm > best:
            break

        best = tm
        curtime += c / income
        income += f

    print "Case #{}: {:.12f}".format(e, best)
    #print "Case #{}:".format(e), best