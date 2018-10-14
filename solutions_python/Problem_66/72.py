t=input()
for it in xrange(1,t+1):
	p=input()
	teams=sorted(zip(map(int, raw_input().split()), xrange(1<<p)))
	for i in xrange(p):
		raw_input()
	matches=[[0] * (1 << p-i) for i in xrange(1, p+1)]
	for m, i in teams:
		for x in xrange(m, p):
			matches[x][i / (1 << x+1)] = 1
	print 'Case #%d: %d' % (it, sum((sum(x) for x in matches)))