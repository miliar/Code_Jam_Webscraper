import sys

def solve(c):
    t, p = 0, 2.0
    C, F, X = [float(f) for f in (sys.stdin.readline().split())]
    while True:
        sg = X/p
        sf1 = C/p
        sf2 = X/(p+F)
        if sg > sf1 + sf2:
            t += sf1
            p += F
        else:
            print 'Case #%d: %.7f' % (c, t+sg)
            return


N = int(sys.stdin.readline())
for c in xrange(1, N+1):
    solve(c)
