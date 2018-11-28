def solve():
    N = int(raw_input())
    m = map(int, raw_input().split())
    y = 0
    d = 0
    for i in xrange(len(m) - 1):
        if m[i] > m[i + 1]:
            y += m[i] - m[i + 1]
        d = max(d, m[i] - m[i + 1])
    s = m[0]
    z = 0
    for i in xrange(1, len(m)):
        z += min(s, d)
        s -= min(s, d)
        s = m[i]
    return "%d %d" % (y, z)

T = int(raw_input())
for i in range(T):
    print 'Case #%d:' % (i + 1), solve()
