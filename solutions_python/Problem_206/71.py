t = int(raw_input())
for kei in xrange(t):
    d, n = (int(x) for x in raw_input().split())
    arr = []
    for i in xrange(n):
        ki, si = (int(x) for x in raw_input().split())
        arr.append((ki, si))
    lo = 0.
    mintime = min((d-ki)/float(si) for ki, si in arr)
    hi = d / mintime
    for i in xrange(100):
        s = (lo + hi) / 2
        ok = True
        for ki, si in arr:
            if s <= si:
                continue
            td = s*ki / (s - si)
            if td < d:
                ok = False
                break
        if ok:
            lo = s
        else:
            hi = s
    print "Case #%d: %.8f" % (kei+1, lo)
