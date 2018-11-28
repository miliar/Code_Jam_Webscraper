import math


pw = [1] * 100
for i in xrange(1, 100):
    pw[i] = pw[i - 1] * 2
LEFT, RIGHT = 1, 2


def divi(x):
    if not x:
        return (0, 0)
    y, r = divmod(x, 2)
    return (y, y - 1 + r)


def solve():
    n, k = map(int, raw_input().split())
    d = int(math.ceil(math.log(n + 1) / math.log(2))) - 1
    if k >= pw[d]:
        return (0, 0)
    d = int(math.ceil(math.log(k + 1) / math.log(2))) - 1
    ss = []
    while k > 1:
        p = pw[d - 1]
        s = LEFT if k + p < pw[d + 1] else RIGHT
        ss.append(s)
        k -= s * p
        d -= 1
    for s in reversed(ss):
        lc, rc = divi(n)
        n = lc if s == LEFT else rc
    return divi(n)


tests = int(raw_input())
for test in xrange(tests):
    r1, r2 = solve()
    print 'Case #%s: %s %s' % (test + 1, r1, r2)
