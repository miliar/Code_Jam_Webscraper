t = int(input())  
for i in range(1, t + 1):
	n2, m1 = [str(s) for s in input().split(" ")]
	m=int(m1)
	n1=list(n2)
	n=len(n1)
	ans=0
	for x in range(1, n+2-m):
		if n1[x-1] in ['-']:
			ans=ans+1
			for y in range(1,m+1):
				if n1[x+y-2] in ['-']:
					n1[x+y-2]='+'
				else :
					n1[x+y-2]='-'		 	
	if '-' in n1:
		print("Case #{}: IMPOSSIBLE".format(i))		
	else:	
		print("Case #{}: {}".format(i,  ans))
