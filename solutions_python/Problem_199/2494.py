t = int(input())
for j in range(t):
	all=[]
	s,n=input().strip().split()
	k=int(n)
	n=len(s)
	for l in range(n):
		if(s[l]=='+'):
			all.append(1)
		else:
			all.append(0)
	
	ans=0
	for i in range(n-k+1):
		if(all[i]==0):
			for l in range(i,i+k):
				all[l] = 1 - all[l]
			ans+=1
	imposs=0
	for i in range(n-k,n):
		if(all[i]==0):
			imposs=1
			break
	if(imposs==1):
		print("Case #"+str(j+1)+":","IMPOSSIBLE")
	else:
		print("Case #"+str(j+1)+":",ans)