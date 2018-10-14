import math
pi=math.pi
t=int(input())
for ij in range(1,t+1):
	n1,k1=input().split(' ')
	n=int(n1)
	k=int(k1)
	c=[]
	d=[]
	for i in range(1,n+1):
		a,b=[int(s) for s in input().split(" ")]
		sa=2*pi*a*b
		c.append((a,b,sa))
	c=sorted(c,reverse=True)
	maxi=0
	for i in range (1,n-k+2):
		area=0
		area+=2*pi*c[i-1][1]*c[i-1][0]+pi*c[i-1][0]**2
		#print(area)
		d=sorted(c[i:], key=lambda element: (element[2]),reverse=True)
		#print(d)
		for i in range (1,k):
			area+=d[i-1][2]
		maxi=max(maxi,area)
		
		
	print("Case #{}: {}".format(ij, maxi))
