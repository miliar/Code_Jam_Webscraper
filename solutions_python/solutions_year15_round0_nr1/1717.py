from __future__ import print_function
inf = open('A-large.in', 'r')
outf = open('A-large.out', 'w')
for t in xrange(1, int(inf.readline()) + 1):
	m, s = inf.readline().split()
	p = out = 0
	for i, n in enumerate(s):
		if i > p:
			out += i - p
			p += i - p
		p += int(n)
	print('Case #%s: %s' % (t, out), file=outf)
