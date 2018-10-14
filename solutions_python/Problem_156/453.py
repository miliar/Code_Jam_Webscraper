t=int(raw_input())
for k in range(1,t+1):
	n=int(raw_input())
	a=map(int,raw_input().split())
	m=max(a)
	l=m
	for i in range(1,m+1):
		sum=i
		for j in range(n):
			if a[j]>i and a[j]%i==0:
				sum+=a[j]/i-1
			elif a[j]>i:
				sum+=a[j]/i
		l=min(l,sum)
	print 'Case #'+str(k)+': '+str(l)

