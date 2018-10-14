from sys import stdin

t, =  map(int,stdin.readline().split())
for i in range(1,t+1):
	n, =  map(int,stdin.readline().split())
	p = []
	for j in range(n):
		a,b =  map(int,stdin.readline().split())
		p+=[[a,b]]
	res=0
	for j in range(n):
		for k in range(n):
			if j==k: continue
			if p[j][0] > p[k][0] and p[j][1] < p[k][1]:
				res+=1
	print "Case #{1}: {0}".format(res,i)
