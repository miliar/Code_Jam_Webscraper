T = int(raw_input())
for t in xrange(1, T + 1):
    (c, f, x) = tuple([float(tmp) for tmp in raw_input().split(' ')])

    s = 0
    ans = 100000000000000.0
    for i in xrange(1000000):
        ans = min(ans, s + x / (2 + i*f))
        s += c / (2 + i*f)
    print 'Case #%d: %.10f' % (t, ans)

