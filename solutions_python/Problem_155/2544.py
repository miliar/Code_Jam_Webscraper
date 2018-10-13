t = int(raw_input())

for x in xrange( t ):

	a, s = raw_input().split()
	a = int(a)
	su = 0
	c = 0
	
	for i in xrange(a+1):
		while su < i:
			c += 1
			su += 1
		su += int(s[i])
	print "Case #%d: %d" % (x+1, c)