T=int(raw_input())
for qq in xrange(1,T+1):
	x,r,c=map(int,raw_input().split())
	if c > r:
		c,r=r,c
	if (r>=x and c>=x-1):
		if ((r - x) * c) % x==0:
			ans='GABRIEL'
		else:
			ans='RICHARD'
	else:
		ans='RICHARD'
	print 'Case #{0}: {1}'.format(qq,ans)
