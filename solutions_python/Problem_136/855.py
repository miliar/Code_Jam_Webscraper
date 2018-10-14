t = int(raw_input().strip())
for i in xrange(t):
    c, f, x = map(float, raw_input().strip().split())
    r = 2.0
    t = 0.0
    ans = x / 2
    while t < ans:
        ans = min(ans, t + x / r)
        t += c / r
        r += f
    print "Case #%d: %.7lf" % (i + 1, ans)
