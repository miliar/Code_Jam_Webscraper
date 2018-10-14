f=file('B-large.in','r')
T=int(f.readline())
for t in range(1,T+1):
	count=0
	a=map(int,f.readline().split())
	n=a[0]
	s=a[1]
	p=a[2]
	b=a[3:]
	b.sort()
	for i in b:
		if(s):
			if((i>=p*3-4 and i!=0) or p==0):
				count+=1
				s-=1
		else:
			if(i>=p*3-2 or p==0):
				count+=1
	print "Case #%d: %d" % (t,count)