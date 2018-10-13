n=int(input())
opts=['Bad magician!','Volunteer cheated!']
for i in range(1,n+1):
	f1=int(input())
	r1=[]
	for j in range(4):
		t=raw_input()
		if j==f1-1:
			r1=map(int,t.split())
	r2=[]
	f2=int(input())
	for j in range(4):
		t=raw_input()
		if j==f2-1:
			r2=map(int,t.split())
	c=0
	ans=-1
	for j in r1:
		for k in r2:
			if k==j:
				c+=1
				ans=j
	print 'Case #%d:' %i,
	if c==1:
		print ans
	elif c==0:
		print opts[1]
	elif c>1:
		print opts[0]
