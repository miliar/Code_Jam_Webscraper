def getVals(t, j):
	i = j
	a = 0
	while i > 0:
		if t[i-1] == 'o':
			break
		else:
			i -= 1
			a += 1

	k = j
	b = 0
	while k < len(t)-1:
		if t[k+1] == 'o':
			break
		else:
			k += 1
			b += 1

	return (a,b)

def heyy(n, k):
	t = '.' * n
	f = 0
	c = 0
	for i in range(k):
		a = []
		for j in range(n):
			if t[j] == '.':
				a.append((getVals(t, j), j))
			else:
				a.append(((-1,-1),-1))
		
		b = []
		for k in a:
			b.append(min(k[0]))

		f = max(b)

		d = []

		for m in range(n):
			if b[m] == f:
				d.append(a[m])

		e = []
		for dd in d:
			e.append(max(dd[0]))		

		c = max(e)

		if len(d) > 1:
			goOn = True
			q = 0

			while goOn:
				if e[q] == c:
					# t[d[q][1]] = 'o'
					tt = list(t)
					tt[d[q][1]] = 'o'
					t = ''.join(tt)
					goOn = False

				q += 1
		else:
			tt = list(t)
			tt[d[0][1]] = 'o'
			t = ''.join(tt) 

	return str(c) + ' ' + str(f)

zz = 1

with open('C-small-1-attempt0.in') as inputFile, open('C-small-1-attempt0.out','w') as outputFile:
	for line in inputFile:
		hell = line.split(' ')
		outputFile.write('Case #'+str(zz)+': '+heyy(int(hell[0]),int(hell[1])) +'\n')
		zz += 1