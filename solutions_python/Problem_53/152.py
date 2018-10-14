import sys

def tobin(n):
    rv = []
    while n:
        rv.insert(0, "1" if (n&1) else "0")
        n >>= 1
    return ''.join(rv)

def test(N, K):
    # N is one-based, K is ordinal
    b = tobin(K)
    if b.endswith('1'*N):
        return "ON"
    return "OFF"

print tobin(3932159)
sys.exit()
T = int(sys.stdin.readline())
for case in xrange(1, T+1):
    N, K = map(int, sys.stdin.readline().strip().split(" "))
    print "Case #%d: %s" % (case, test(N, K))
