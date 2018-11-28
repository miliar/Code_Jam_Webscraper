import math
t = int(input())
for i in range(1, t + 1):
	
	n, m = [int(s) for s in input().split(" ")]
	m=int(m)
	if m>1: 
		a=[]
		a.append(n)
		for j in range (1,m):
			a=sorted(a)
			b=int(a[-1]/2)
			c=int(a[-1]/2-0.5)
			del a[-1]
			a.append(b)
			a.append(c)
		a=sorted(a)
		b=int(a[-1]/2)
		c=int(a[-1]/2-0.5)	
		print("Case #{}: {} {}".format(i, b, c))
	else:
		n=int(n)
		print("Case #{}: {} {}".format(i, int(n/2), int(n/2-0.5)))
