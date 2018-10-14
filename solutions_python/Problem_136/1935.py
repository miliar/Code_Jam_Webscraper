import sys

def calc(C, F, X, n_farms):
    denum = 2.0
    total = 0
    for i in xrange(n_farms):
        total += C / denum
        denum += F
    return total + X / denum

def tcase():
    C, F, X = map(float, sys.stdin.readline().split())
    low, high = 0, 10**6
    while (high - low) > 1:
        mid = (low + high) / 2
        if calc(C, F, X, mid-1) > calc(C, F, X, mid):
            low = mid
        else:
            high = mid
    if high == 10**6:
        print >>sys.stderr, 'Too low'
    print calc(C, F, X, low)

T = int(sys.stdin.readline())
for i in xrange(T):
    print 'Case #%d:' % (i+1),
    print >>sys.stderr, i
    tcase()