#!/home/balazs/anaconda2/bin/python

t = int(raw_input())
for i in xrange(t):
    d, n = map(int, raw_input().split(' '))
    ks, ss = zip(*[map(int, raw_input().split(' ')) for _ in xrange(n)])
    print "Case #{0}: {1:.6f}".format(1 + i, d / max(float(d - k) / s for k, s in zip(ks, ss)))
