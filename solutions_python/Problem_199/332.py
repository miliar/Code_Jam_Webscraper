for t in xrange(1,input()+1):
	s,k=raw_input().split()
	k=int(k)
	n=len(s)
	happy=[False]*n
	for i in xrange(n):
		happy[i]=(s[i]=='+')
	end=n-1
	ans=0
	for i in xrange(n-1,k-2,-1):
		if not happy[i]:
			for j in xrange(k):
				happy[i-j]=(not happy[i-j])
			ans+=1
	flag=True
	for i in xrange(n):
		if not happy[i]:
			flag=False
	print 'Case',('#'+str(t)+':'),(ans if flag else 'IMPOSSIBLE')


