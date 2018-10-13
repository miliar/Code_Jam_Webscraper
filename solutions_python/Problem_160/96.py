for t in xrange(input()):
    b, n = map(int, raw_input().split())
    m = map(int, raw_input().split())
    beg, end = 0, int(1e16)
    while beg < end:
        cen = (beg + end) / 2
        if sum(cen/x+1 for x in m) >= n:
            end = cen
        else:
            beg = cen + 1
    r = [i for i,x in enumerate(m) if beg%x==0]
    res = r[::-1][sum(beg/x+1 for x in m) - n]
    print 'Case #%d: %d' % (t+1, res+1)
