t = int(input())
for case in range(t):
	st = input()
	n = len(st)
	d = {}
	for i in range(n):	
		d[i] = int(st[i])
	
	c = 0
	for i in range(n-1):
		if d[i] > d[i+1]:
			c =1
			break
	if c==0:
		s = st
	else:
		while i > 0 and d[i]==d[i-1]:
			i-=1
		s =""
		for j in range(i):
			s+=st[j]
		if d[i]>1:
			s+=str(d[i]-1)
			s+= ('9'*(n-i-1))
		else:
			s = '9'*(n-1)


	print("Case #"+str(case+1)+": "+ s)