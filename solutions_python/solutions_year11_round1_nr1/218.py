import sys

ts = int(sys.stdin.readline())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b);

for t in xrange(ts):
    n, pd, pg = map(int, sys.stdin.readline().split())
    x = gcd(100, pd)
    if (pg == 100 and pd != 100) or (pg == 0 and pd != 0):
        print "Case #%d: Broken" % (t+1)
    else:
        if 100 / x <= n:
            print "Case #%d: Possible" % (t+1)
        else:
            print "Case #%d: Broken" % (t+1)