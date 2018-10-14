

t = int(input())
for case in range(t):
	[s,y]= input().split()
	k = int(y)
	n = len(s)
	d = {}
	for i in range(n):
		if s[i]=='+':
			d[i]=0
		else:
			d[i]=1
	ans=0
	#print(d)
	for i in range(n-k+1):
		if d[i]==1:
			ans+=1
			for j in range(i,i+k):
				if d[j]==0:
					d[j]=1
				else:
					d[j]=0
		#print(d)
	c = 0
	for i in range(n-k+1,n):
		if d[i]==1:
			c = 1
			break

	if c ==0:
		fin = str(ans)
	else:
		fin = "IMPOSSIBLE"



	print("Case #"+str(case+1)+": "+ fin)

	

