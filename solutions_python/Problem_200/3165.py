size=input()
for no in range(0,size):
	test=input()
	d=[]
	i=test%10
	while(test!=0):
		d.append(i)
		test=test/10
		i=test%10
	d.reverse()
	last=0
	for i in range(0,len(d)-1):
		if(d[i+1]<d[i]):
			d[i]=d[i]-1
			last=1
			break
	for j in range(i+1,len(d)):
		if(last==0):
			break
		d[j]=9
	for j in range(i+1,0,-1):
		if(len(d)==1):
			break
		if(d[j]<d[j-1]):
			d[j-1]=d[j-1]-1
			d[j]=9
	x=0
	for i in d:
		x=x*10+i
	print "Case #"+str(no+1)+": "+str(x)