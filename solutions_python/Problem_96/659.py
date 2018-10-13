for T in xrange(input()):
	r = map(int,raw_input().split())
	N,S,p = r[:3]
	t = r[3:]
	x = 0
	for i in t:
		if i>=p+2*max(0,p-1):
			x+=1
		elif i>=p+2*max(0,p-2) and S>0:
			x+=1
			S-=1
	print 'Case #%d: %d'%(T+1,x)
