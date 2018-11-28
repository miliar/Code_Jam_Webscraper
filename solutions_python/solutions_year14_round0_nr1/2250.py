for t in xrange(input()):
	A1=input()
	a=[]
	b=[]
	c=set()
	for _ in xrange(4):
		temp=map(int,raw_input().split())
		a.append(temp)
	A2=input()
	for _ in xrange(4):
		temp=map(int,raw_input().split())
		b.append(temp)
	res=0
	numberAns=0
	c=set(a[A1-1])
	for i in xrange(4):
		if b[A2-1][i] in c:
			numberAns=numberAns+1
			res=b[A2-1][i]
	if numberAns==1:
		print "Case #"+str(t+1)+": "+str(res)
	elif numberAns==0:
		print "Case #"+str(t+1)+": Volunteer cheated!"
	elif numberAns>1:
		print "Case #"+str(t+1)+": Bad magician!"