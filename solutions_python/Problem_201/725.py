numruns = int(input())
for run in range(numruns):
	dat = input().split()
	n = int(dat[0])
	k = int(dat[1])
	c1,c2 = 1,0
	i=0
	while k>2**i:
		tn,t1,t2=(n-1)//2,c1,0
		if n//2==tn:
			t1+=c1+c2
		else:
			t2+=c1+c2
		if (n+1)//2==tn:
			t1+=c2
		else:
			t2+=c2
		n,c1,c2 = tn,t1,t2
		k-=2**i
		i+=1
	if k<=c2:
		print('Case #'+str(run+1)+': '+str(max(n//2,(n+1)//2))+' '+str(min(n//2,(n+1)//2)))
	else:
		print('Case #'+str(run+1)+': '+str(max(n//2,(n-1)//2))+' '+str(min(n//2,(n-1)//2)))
	