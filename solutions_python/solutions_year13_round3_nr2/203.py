ntest = int(raw_input())
for itc in xrange(ntest):
	print 'Case #%d:' % (itc+1),
	x, y = map(int,raw_input().split())
	first = 'WE'
	if (x < 0):
		first = 'EW'
		x *= -1
	then = 'SN'
	if (y < 0):
		then = 'NS'
		y *= -1
	print first * x + then * y	
	 
