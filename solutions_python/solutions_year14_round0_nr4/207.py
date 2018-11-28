rl = lambda: map(float, raw_input().split())


def solve(n, a, b):
    # a.sort(reverse=True)
    # b.sort(reverse=True)
    a.sort()
    b.sort()
    c = [(x, 1) for x in a] + [(x, -1) for x in b]
    c.sort()
    s = ss = 0
    for x, k in c:
        s += k
        ss += k
        if s < 0:
            s = 0
        if ss > 0:
            ss = 0

    r = 0
    for k in xrange(n):
        r = max(
            r,
            sum(1 for i, j in zip(a[k:], b) if i > j)
        )
    return r, s


t = input()
for nt in xrange(1, t + 1):
    n = input()
    a = rl()
    b = rl()
    print "Case #%d: %d %d" % ((nt,) + solve(n, a, b))
