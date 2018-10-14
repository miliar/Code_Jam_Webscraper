
z = int(raw_input())

for tc in xrange(z):
	line = raw_input().split()
	n = int(line[0])
	k = int(line[1])
	p = 2**n
	res = 'OFF'
	if (k+1)%p == 0: res = 'ON'
	print 'Case #%d: %s' % (tc+1, res)

