import sys
c = int(raw_input())

for case in xrange(c):
    r, t = map(int, sys.stdin.readline().split())
    formula = lambda x: x*(2*r+1) + 2*x*(x-1)
    upper = 1
    while (formula(upper) <= t): upper *= 2

    val = 0
    while (upper):
        if formula(upper+val) <= t:
            val += upper
        upper /= 2
    print "Case #%d:" % (case + 1), val