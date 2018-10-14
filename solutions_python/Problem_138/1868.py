t=input()
c=1
while t!=0:
	n=input()
	a=raw_input().split()
	for i in range(0,n):
		a[i] = float(a[i])
	a.sort()
	b=raw_input().split()
	for i in range(0,n):
		b[i] = float(b[i])
	b.sort()
	ans1=0
	x=n
	i=0
	j=0
	while(i!=n):
		if(a[i]<b[j]):
			i+=1
			x-=1
		else:
			i+=1
			j+=1
			ans1+=1
	j=0
	i=0
	while j!=n:
		if(a[i]<b[j]):
			i+=1
			j+=1
		else:
			j+=1
	ans2=n-i
	print "Case #%d"%c+": %d %d" %(ans1,ans2)
	c+=1
	t-=1
