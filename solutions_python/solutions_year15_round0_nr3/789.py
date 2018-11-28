def prod(a,b):
	prodtab = [[1,2,3,4],[2,-1,4,-3],[3,-4,-1,2],[4,3,-2,-1]]
	if a<0:
		return -prodtab[abs(a)-1][abs(b)-1]
	elif b<0:
		return -prodtab[abs(a)-1][abs(b)-1]
	else:
		return prodtab[abs(a)-1][abs(b)-1]

def parseString(s):
	x = [0]*len(s)
	for i in range(0,len(s)):
		if s[i] == 'i':
			x[i] = 2
		elif s[i] == 'j':
			x[i] = 3
		elif s[i] == 'k':
			x[i] = 4
		else:
			x[i] = 1
	return x

def canyousplit(s):
	p = parseString(s)
	l = p[0]
	u = p[len(p)-1]
	i = 1
	j = len(p) - 2
	flag = 'NO'
	if l == 2 and u == 4:
		m = p[i]
		while i+1<=j:
			m = prod(m,p[i+1])
			i=i+1
		if m == 3:
			flag ='YES'
	else:
		while i<len(p):
			if prod(l,p[i]) == 2:
				i=i+1
				break
			else:
				l = prod(l,p[i])
				i=i+1

		while j>=0:
			if prod(p[j],u) == 4:
				j=j-1
				break
			else:
				u = prod(p[j],u)
				j=j-1

		if(j<i):
			flag ='NO'
		else:
			m = p[i]
			while i+1<=j:
				m = prod(m,p[i+1])
				i=i+1
			if m == 3:
				flag = 'YES'
			else:
				flag = 'NO'


	return flag




T = int(raw_input());


for i in range(0,T):
	line = raw_input()
	n = int(line.split(' ')[1])
	line = raw_input()
	a = line*n
	print 'Case #'+str(i+1)+':', canyousplit(a)
