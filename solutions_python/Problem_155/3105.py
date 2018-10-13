t=int(input())
for i in range(t):
	s=input().split()
	n=int(s[0])
	a=[]
	for j in range(n+1):
		a.append(int(s[1][j]))
	ans=0
	current=a[0]
	for j in range(1,n+1):
		if current>=j:
			current+=a[j]
		else:
			ans=ans+j-current
			current=j+a[j]
	print('Case #'+str(i+1)+': '+str(ans))