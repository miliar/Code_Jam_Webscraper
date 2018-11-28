import sys
sys.setrecursionlimit(10000)

def memoize(f):
    d = {}
    def memoized(*args):
        if args not in d:
            d[args] = f(*args)
        return d[args]
    return memoized

@memoize
def choose(n,k):
    if k < 0: return 0
    if k > n: return 0
    if n <= 1 and k <= 1: return 1
    return choose(n-1,k) + choose(n-1,k-1)

@memoize
def puresets(n,k):
    if n == 1:
        if k == 0: return 1
        else: return 0
    s = 0
    for i in xrange(0, k):
        s += (puresets(k,i) * choose(n-k-1, k-i-1)) % 100003
    return s

def ans(n):
    return sum(puresets(n,x) for x in xrange(n)) % 100003

getnum = lambda: [int(x) for x in raw_input().split()]
T = getnum()[0]
for testid in range(T):
    print "Case #%d: %d" % (testid+1, ans(getnum()[0]))
