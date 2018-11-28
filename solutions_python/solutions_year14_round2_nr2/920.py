for r in xrange(input()):
	a,b,k=(int(x) for x in raw_input().split(' '))
	c=0
	for i in xrange(a):
		for j in xrange(b):
			if i&j<k: c+=1
	print 'Case #%d: %d'%(r+1,c)
