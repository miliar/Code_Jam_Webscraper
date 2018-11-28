def solve(n,s,p,ts):
    assert len(ts)==n
    a = max(3*p - 2, p)
    b = max(a - 2, p)
    result = 0
    for t in ts:
        if t >= a:
            result += 1
        elif t >= b:
            if s > 0:
                s -= 1
                result += 1
    return result


import sys
it = iter(sys.stdin)
next(it)
for i, line in enumerate(it, 1):
    xs = map(int, line.split())
    (n,s,p),ts = xs[:3], xs[3:]
    r = solve(n,s,p,ts)
    print u'Case #{}: {}'.format(i, r)
