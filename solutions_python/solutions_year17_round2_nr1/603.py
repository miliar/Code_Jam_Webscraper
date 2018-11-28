

for case in xrange(1, int(raw_input()) + 1):
    print 'Case #{}:'.format(case),

    d, n = map(int, raw_input().split())
    b = 0

    for i in xrange(n):
        x, v = map(float, raw_input().split())
        b = max(b, (d - x) / v)

    print '%.6f'%(d / b)
