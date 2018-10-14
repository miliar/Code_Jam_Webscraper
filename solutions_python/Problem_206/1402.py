t = int(raw_input())
for i in xrange(1, t + 1):
    n, m = [s.strip() for s in raw_input().split(" ")]
    n = int(n)
    m = int(m)
    others = []
    osp = []
    for j in xrange(1, m + 1):
        k, s = [s.strip() for s in raw_input().split(" ")]
        k = int(k)
        s = float(s)
        ms = (n-k)/s
        osp.append(ms)
    result = n / max(osp)
    print "Case #{}:".format(i),
    print "{0:6f}".format(result)
