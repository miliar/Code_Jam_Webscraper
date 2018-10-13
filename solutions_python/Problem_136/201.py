def solve():
    c, f, x = map(float, raw_input().split())
    m = x / 2.
    t, s = 0, 2.
    for i in xrange(1, 100000000):
        t += c / s
        s += f
        mm = t + x / s
        if mm >= m:
            break
        m = mm
    return m

t = input()
for nt in xrange(1, t + 1):
    print 'Case #%d: %.8f' % (nt, solve())
