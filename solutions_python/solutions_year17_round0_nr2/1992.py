t = int(input())  # read a line with a single integer
for l in range(1, t + 1):
	n1=int(input())
	n=[int(s) for s in str(n1)]
	m=len(str(n1))
	ans=1
	while ans>0:
		ans=0
		for i in range(1,m):
			if n[i-1]>n[i]:
				for j in range(i,m):
					n[j]=9
				n[i-1]=n[i-1]-1
				ans=1
	a = ''.join(map(str, n))
	print("Case #{}: {}".format(l,int(a)))
