T=int(raw_input())
t=T
while t:
	n=int(raw_input())
	m=map(int,raw_input().split())
	mdiff=0
	bval=0
	rate=0
	ans1=0
	ans2=0
	for i in range(0,n-1):
		if (m[i]-m[i+1])>mdiff:
			mdiff=m[i]-m[i+1]
			bval=m[i]
			rate=mdiff/10.0
		if (m[i]-m[i+1])>0:
			ans1+=(m[i]-m[i+1])
	for i in range(0,n-1):
		if (m[i]-m[i+1])<=mdiff:
			if m[i]>mdiff:
				ans2+=mdiff
			else:
				ans2+=m[i]
	print 'Case #'+str(T-t+1)+': '+str(ans1)+' '+str(ans2)
	t-=1