def _gcd(x,y):
    while x:
        x, y = y % x, x
    return y

def gcd(*ns):
    ans = ns[0]
    for i in xrange(1, len(ns)):
        ans = _gcd(ans, ns[i])
    return ans

def calc_cycle(xs):
    m = min(xs)
    xs = map(lambda x:(x-m), sorted(xs))[1:]
    return gcd(*xs)

def solve(*xs):
    xs = sorted(xs)
    cycle = calc_cycle(xs)
    if cycle == 1:
        return 0
    if xs[0] % cycle == 0:
        return 0
    return cycle-(xs[0] % cycle)

import sys

def main():
    f = sys.stdin
    C = int(f.readline())
    for c in xrange(C):
        split = map(int, f.readline().split())
        N, es = split[0], split[1:]
        assert N == len(es)
        print "Case #%d: %d" % (c+1, solve(*es))

if __name__ == "__main__":
    main()
