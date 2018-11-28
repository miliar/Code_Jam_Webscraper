def calc(d):
        n = 0
        for a in sorted(d.keys()):
                for k in d:
                        if d[k] < d[a]:
                                n += 1
                del d[a]
        return n

T = input()
for i in xrange(T):
        N = input()
        d = {}
        for j in xrange(N):
                a, b = [int(n) for n in raw_input().split()]
                d[a] = b
	print "Case #%i: %s" % (i+1, calc(d))

