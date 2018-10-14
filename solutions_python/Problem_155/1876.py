t=int(raw_input())
for _ in xrange(1,t+1):
	t-=1
	a,b=raw_input().split()
	l=map(int,b)
	s=l[0]
	ans=0
	for i in xrange(1,int(a)+1):
		if s<i:
			ans+=i-s
			s+=i-s
		s+=l[i]
	print 'Case #%d: %d' %(_,ans)