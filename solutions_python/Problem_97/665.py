ll = open('/Users/pittaya/Downloads/C-large.in').readlines()
numcase = ll[0]

def get_pairs():
	pass

i = 1
for l in ll[1:]:
	(a, b) = l.strip().split(' ')
	a = int(a)
	b = int(b)
	s = set()
	for n in xrange(a, b+1):
		t = str(n)
		for tt in xrange(1, len(t)):
			m = int(t[-tt:] + t[:-tt])
			if (m != n) and (n < m) and (m >= a) and (m <= b):
				s.add('%s,%s' % (n, m))
	print "Case #%d: %d" % (i, len(s))
	i += 1