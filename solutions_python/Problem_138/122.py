import sys
f = sys.stdin
T = int(f.readline().strip())
for i in range(1,T+1):
    N = int(f.readline().strip())
    naomi = [float(x) for x in f.readline().strip().split(' ')]
    ken   = [float(x) for x in f.readline().strip().split(' ')]
    naomi = sorted(naomi, reverse=True)
    ken   = sorted(ken,   reverse=True)
    res = 0
    l, r, a = 0, 0, 0
    while a < N:
        #print 'l %d r %d' % (l,r)
        if naomi[l] > ken[r]:
            res += 1
            l += 1
        else:
            r += 1
            l += 1
        a += 1
    res2 = 0
    l, r, a = 0, 0, 0
    naomi = sorted(naomi)
    ken   = sorted(ken)
    while a < N:
        #print 'l %d r %d' % (l,r)
        if naomi[l] < ken[r]:
            l += 1
        else:
            res2 += 1
            r += 1
            l += 1
        a += 1
    sys.stdout.write('Case #%d: %d %d\n' % (i, res2, res))