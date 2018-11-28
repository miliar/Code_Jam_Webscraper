T = int(raw_input())
s = ''
for cnt in xrange(T):
	n, k  = [int(i) for i in raw_input().split()]
	c = 1 << n
	if ((k + 1) % (c)) == 0:
		s = 'ON'
	else:
		s = 'OFF'
	print 'Case #%d: %s' % (cnt+1,s)
