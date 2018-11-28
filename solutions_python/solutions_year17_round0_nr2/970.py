f = open('B-large.in', 'r')
g = open('data.out', 'w')

t = int(f.readline())
for i in range(0, t):
	ok = True
	n = f.readline()
	x = list(n)
	if(x[len(x) -1] == '\n'):
		x.pop()
	if len(n) < 2:
		ok = False
	while ok:
		ok = False
		for j in range(len(x) - 1, 0, -1):
			if int(x[j]) < int(x[j-1]):
				ok = True
				x[j - 1] = str(int(x[j - 1]) - 1)
				for k in range(j, len(x)):
					x[k] = '9'
			
	g.write('Case #' + str(i + 1) + ': ')
	for j in x:
		if ok: 
			g.write(j)
		else:
			if j != '0':
				ok = True
				g.write(j)
	g.write('\n')
f.close()
g.close()