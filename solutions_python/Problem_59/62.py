def mkset(l):
    s = set()
    for x in l:
        for p in xrange(len(x)+1):
            s.add(tuple(x[0:p]))
    return s

getnum = lambda: [int(x) for x in raw_input().split()]
T = getnum()[0]
for testid in range(T):
    [n,m] = getnum()
    existing = mkset(raw_input().strip().split("/")[1:] for i in xrange(n))
    tocreate = mkset(raw_input().strip().split("/")[1:] for i in xrange(m))
    if () not in existing: existing.add(())
    print "Case #%d: %d" % (testid+1, len(tocreate - existing))
