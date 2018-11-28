
def flip(t,pos,k):
	s = list(t)
	j=pos
	for i in range(k):
		if s[j]=='+':
			s[j]='-'
		else:
			s[j]='+'
		j+=1
	return s

f = open('A-small-attempt1.in')
#f=  open('test.txt')
T = int(f.readline())
for case in range(T):
	l = f.readline().split()
	pancakes = l[0]
	N = len(pancakes)
	K = int(l[1])

	s = ['+']*N
	table={}
	table[''.join(s)]=0
	Q = [s]
	while len(Q) > 0:
		t = Q[0]
		n = table[''.join(t)]
		del Q[0]
		for i in range(0,N-K+1):
			t2 = flip(t,i,K)
			if not ''.join(t2) in table:
				Q.append(t2)
				table[''.join(t2)] = n + 1
	
	#print table
	if pancakes in table:
		print 'Case #'+str(case+1)+": "+str(table[pancakes])
	else:
		print 'Case #'+str(case+1)+": IMPOSSIBLE"
