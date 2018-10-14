if 1:
    from sys import *
    from functools import *
    from collections import *
    from itertools import *
    from functools import *
    from heapq import *
    from math import *
    xr = xrange

    def print_args(*args, **kwargs):
        return ','.join(value for value in [','.join(map(repr, args)),','.join("%s=%s" % (k, repr(v)) for k, v in kwargs.items())] if value)

    def print_result(before=False, after=True):
        def fc(func):
            @wraps(func)
            def f(*args, **kwargs):
                if before:
                    print "%s(%s)"      % (func.__name__, print_args(*args, **kwargs))
                r = func(*args, **kwargs)
                if after:
                    print "%s(%s) = %s" % (func.__name__, print_args(*args, **kwargs), r)
                return r
            return f
        return fc

    def memoize(function):
        memo = {}
        @wraps(function)
        def f(*args):
            key = args
            if key not in memo:
                memo[key] = function(*args)
                if not (len(memo) & 32767):
                    print >>stderr, "memo", function.__name__, len(memo)
            return memo[key]
        f.memo = memo
        return f

    def printErr(error):
        print >>stderr, error

    def line():
        return raw_input().strip()

    def parts(f=int):
        return map(f, line().split())

    def qparts(f=int):
        data = line().split()
        return data[0], map(f, data[1:])

def solve():
    n, c, m = parts()
    b = [0]*c
    p = [0]*n
    for _ in xr(m):
        pi, bi = parts()
        b[bi-1] += 1
        p[pi-1] += 1

    rides = max(b)
    s = 0
    for i, x in enumerate(p):
        s += x
        rides = max(rides, int(ceil(s/float(i+1))))

    promo = 0
    for x in p:
        if x > rides:
            promo += (x-rides)

    return (rides, promo)

def main():
    t = int(raw_input())
    for i in xrange(t):
        a, b = solve()
        print "Case #{}: {} {}".format(i+1, a, b)
main()
