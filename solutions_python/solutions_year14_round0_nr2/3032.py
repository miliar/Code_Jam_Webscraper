import sys
def solve(x):
    C, F, X = (float(a) for a in raw_input().split(' '))
    def f(cps):
        if X/cps > C/cps + X/(cps+F):
            return min(X/cps, C/cps + f(cps+F))
        return X/cps
    print "Case #%d: %f" % (x, f(2.0))

sys.setrecursionlimit(150000000)
T = int(raw_input())
for i in xrange(T):
    solve(i+1)
