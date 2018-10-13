if 1:
    from sys import *
    from functools import *
    from collections import *
    from itertools import *
    from functools import *
    from heapq import *
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

    def line():
        return raw_input().strip()

    def parts(f=int):
        return map(f, line().split())

    def qparts(f=int):
        data = line().split()
        return data[0], map(f, data[1:])


def _groups(p):
    for vals in product(xrange(p+1), repeat=p):
        if any(vals) and sum(v * i for i, v in enumerate(vals)) % p == 0:
            yield vals

@memoize
def groups(p):
    return list(_groups(p))

def sub(a, b):
    return [A - B for A, B in zip(a, b)]

@memoize
def ans(p, *c):
    if sum(c) == 0: return 0
    if c[0]: return c[0] + ans(p, 0, *c[1:])
    res = 1
    for g in groups(p):
        if all(c[i] >= g[i] for i in xrange(p)):
            res = max(res, 1 + ans(p, *sub(c, g)))
    return res

for cas in xrange(1,1+input()):
    ans.memo.clear()
    n, p = parts()
    c = Counter(v % p for v in parts())
    c = [c[i] for i in xrange(p)]
    print "Case #%s: %s" % (cas, ans(p, *c))
