for t in xrange(input()):
    _, p = input(), map(int, raw_input().split())
    print 'Case #%d: %d' % (t+1, min(m+sum((x-1)/m for x in p) for m in xrange(1,max(p)+1)))
