import sys

input = sys.stdin
T=int(input.readline())
for i in xrange(1,T+1):
    N, K = map(int, input.readline().split())
    if (K+1) % (2**N) == 0:
        res = 'ON'
    else:
        res = 'OFF'
    print "Case #%s: %s" % (i, res)
