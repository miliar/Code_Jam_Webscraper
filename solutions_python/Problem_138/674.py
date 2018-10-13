def check(a,b,n):
	j=0
	k=0
	
	i=0
	while(i<n and j<n):	
		if(a[i]>b[j]):
			k=k+1
			i=i+1
			j=j+1
		else:
			j=j+1
	return k

t=int(raw_input())
for i in xrange(t):
	n=int(raw_input())
	a=map(float,raw_input().split())
	b=map(float,raw_input().split())
	a.sort(reverse=True)
	b.sort(reverse=True)
	p=check(a,b,n)
	q=check(b,a,n)
	print "Case #%d: %d %d" %(i+1,p,n-q)
