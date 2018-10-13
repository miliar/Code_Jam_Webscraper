import sys
fin = sys.stdin

T = int(fin.readline())

for i in xrange(T):
    A, B = map(int, fin.readline().split())
    d = {}
    l = len(str(A))
    for q in xrange(A, B+1):
        s = str(q) * 2
        m = min(s[i:i+l] for i in xrange(l) if s[i] != '0')
        o = d.get(m, 0)
        d[m] = o + 1
    #print d
    ans = 0
    for t in d.itervalues():
        ans += t * (t - 1) / 2
    print 'Case #{0}: {1}'.format(i+1, ans)
