t=int(input())
for z in range(t):
	r,c=map(int,input().split(" "))
	l=[]
	for k in range(r):
		n=list(input())
		l.append(n)
	for i in range(r):
		m='?'
		y=0
		for j in range(c):
			if(l[i][j]=='?'):
				l[i][j]=m
			else:
				m=l[i][j]
				y=1
		if(y==0 and i!=0):
			l[i]=l[i-1]
		if(i==0 and y==0):
			l[i]=l[i+1]

	for i in range(r-1,-1,-1):
		m='?'
		y=0
		for j in range(c-1,-1,-1):
			if(l[i][j]=='?'):
				l[i][j]=m
			else:
				m=l[i][j]
				y=1
		if(i==(r-1) and y==0):
			l[i]=l[i-1]
		if(i!=(r-1) and y==0):
			l[i]=l[i+1]

	print("Case #%d:"%(z+1))
	for i in range(len(l)):
		print(*l[i],sep="")
	


	#print('\n'.join([''.join(['{:1}'.format(item) for item in row]) 
     # for row in l]))
	
