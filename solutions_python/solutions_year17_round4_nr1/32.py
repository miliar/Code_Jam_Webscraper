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
    n, p = parts()
    a = parts()

    cnt = [0]*p
    for x in a:
        cnt[x%p] += 1

    ans = cnt[0]
    if p == 2:
        ans += ceil(cnt[1]/float(p))
    elif p == 3:
        a1 = cnt[1]
        a2 = cnt[2]
        d = min(a1, a2)
        ans += d
        a1 -= d
        a2 -= d
        ans += ceil((a1+a2)/float(p))
    elif p == 4:
        a1 = cnt[1]
        a2 = cnt[2]
        a3 = cnt[3]
        ans += a2 / 2
        a2 = a2 % 2
        d = min(a1, a3)
        ans += d
        a1 -= d
        a3 -= d
        d = a1+a3
        if a2 == 1:
            ans += 1
            d = max(0, d-2)
        ans += ceil(d/float(p))

    return int(ans)


def main():
    t = int(raw_input())
    for i in xrange(t):
        print "Case #{}: {}".format(i+1, solve())
main()
