import re
L, D, N = [int(x) for x in raw_input().split()]
d = []
for i in xrange(D):
	d.append(raw_input().strip())
for i in xrange(N):
	p = raw_input().strip()
	p = p.replace('(','[').replace(')',']')
	r = re.compile(p)
	c = 0
	for s in d:
		if r.match(s):
			c += 1
	print 'Case #%d: %d' % (i+1, c)
