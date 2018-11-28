T=int(raw_input())

for t in range(T):
	A,N=[int(x) for x in raw_input().split()]
	L=[int(x) for x in raw_input().split()]
	L.sort()
	
	if A==1:
		print "Case #%d: %d"%(t+1,N)
		continue
		
	ans=0
	for i in range(N):
		if A>L[i]:
			A+=L[i]
			continue
		z=0
		while A<=L[i]:
			A+=A-1
			z+=1
		if z<N-i:
			ans+=z
			A+=L[i]
		else:
			ans+=N-i
			break
			
	print "Case #%d: %d"%(t+1,ans)