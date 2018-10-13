T = int(raw_input())
for tt in xrange(T):
    d, n = map(int, raw_input().split())
    ks = []
    for _ in xrange(n):
        kk, ss = raw_input().split()
        ks.append((int(kk), float(ss)))
    ks.sort(key=lambda x: -x[0])
    last_t = (d - ks[0][0]) / ks[0][1]
    for i in xrange(1, len(ks)):
        k, s = ks[i]
        t = (d - k) / s
        if last_t < t:
            last_t = t
    print 'Case #%s: %.6f' % (tt+1, d / last_t)
