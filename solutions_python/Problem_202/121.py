def score(l):
	s = 0
	for i in range(n):
		for j in range(n):
			if l[i][j] == 'o':
				s+=2
			if l[i][j] == '+' or l[i][j] == 'x':
				s+=1
	return s	

t = int(input())
for t_index in range(t):
	n,m = input().split()
	n = int(n)
	m = int(m)
	l = []
	l_beg = []
	for _ in range(n):
		l.append([])
		l_beg.append([])
		for _ in range(n):
			l[-1].append('')
			l_beg[-1].append('')
	for _ in range(m):
		c,i,j = input().split()
		i = int(i) - 1
		j = int(j) - 1
		l[i][j] = c
		l_beg[i][j] = c
	
	l0 = l[0]
	index = -1
	if l0.count('o')==0:
		if l0.count('x')==1:
			for i in range(n):
				if l0[i]=='x':
					l0[i]='o'
					index = i
				if l0[i]=='':
					l0[i]='+'
				
		else:
			p = False
			for i in range(n):
				if l0[i]=='':
					if not p:
						l0[i]='o'
						index = i
						p = True
					else:
						l0[i]='+'
			if not p:
				l0[0] = 'o'
				index = 0
	else:
		for i in range(n):
			if l0[i]=='':
				l0[i]='+'
			if l0[i]=='o':
				index = i
	
	i = 0
	if index != n-1:
		for j in range(1,n):
			if i==index:i+=1
			l[j][i] = 'x'
			i+=1
	else:
		for j in range(1,n):
			l[j][n-1-j] = 'x'
			i+=1
	
	ln = l[-1]
	for i in range(1,n-1):
		ln[i] = '+'

	s = score(l)
	
	changes = []
	for i in range(n):
		for j in range(n):
			if l[i][j] != l_beg[i][j]:
				changes.append((l[i][j],i+1,j+1))
	
	

	print("Case #"+str(t_index+1)+": "+str(s)+" "+str(len(changes)))
	for r in changes:
		print(r[0]+" "+str(r[1])+" "+str(r[2]))
