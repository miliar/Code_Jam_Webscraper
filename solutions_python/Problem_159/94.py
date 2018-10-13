for t in xrange(input()):
    n = input()
    a = map(int, raw_input().split())
    last = res = maks_diff = res2 = 0
    for x in a:
        res += max(0, last-x)
        maks_diff = max(maks_diff, last-x)
        last = x
    for x in a[:-1]:
        res2 += min(x, maks_diff)
    print 'Case #%d: %d %d' % (t+1, res, res2)
