t = int(raw_input())
for i in xrange(t):
	nk = map(int, raw_input().split())
	n = nk[0]
	k = nk[1]
	np = 2 ** n
	s = ''
	if (k % np == np - 1):
		s = 'ON'
	else:
		s = 'OFF'
	print 'Case #%i: %s' % (i+1, s)
