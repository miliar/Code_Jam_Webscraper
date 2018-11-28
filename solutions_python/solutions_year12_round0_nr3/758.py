cases = raw_input()
for case in xrange(int(cases)):
    A, B = map(int, raw_input().strip().split())
    pairs = set()
    for n in xrange(A, B+1):
        n = str(n)
        for i in xrange(len(n)-1, 0, -1):
            m = n[i:] + n[:i]
            if not m.startswith('0') and int(m) <= B and int(n) < int(m):
                pairs.add((n, m))
    
    print 'Case #%d: %s' % (case + 1, len(pairs))
