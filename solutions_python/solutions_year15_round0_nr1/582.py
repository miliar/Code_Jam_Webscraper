for t in range(input()):
	S=map(int,raw_input().split()[1])
	c=r=0
	for n,s in enumerate(S,1):
		c+=s
		r+=max(n-c,0)
		c=max(c,n)
	print 'Case #%d: %d'%(t+1,r)