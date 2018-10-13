
t = input()
for i in range(t):
	n,m = map(int,raw_input().split())
	#print n,m
	l = []
	for j in range(n):
		l.append(map(int,raw_input().split()))
	#print l
	r = [0]*n
	c = [0]*m
	for j in range(n):
		for k in range(m):
			if l[j][k] > r[j]:
				r[j] = l[j][k]
			if l[j][k] > c[k]:
				c[k] = l[j][k]
				
	#print r,c
	possible = True
	for j in range(n):
		for k in range(m):
			if (l[j][k] < r[j]) and (l[j][k] < c[k]):
				possible = False
				break
	if possible:
		print "Case #"+str(i+1)+": YES"
	else:
		print "Case #"+str(i+1)+": NO"