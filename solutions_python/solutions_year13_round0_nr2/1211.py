fin = open('a.in', 'r')
fout = open('a.out', 'w')

T = eval(fin.readline())

def getline():
	return [eval(num) for num in fin.readline().split(' ')]

for t in range(T):
	n, m = getline()
	a = []
	for i in range(n):
		a.append(getline())

	b = []
	for i in range(n):
		maxh = max(a[i])
		b.append([maxh] * m)
	
	for i in range(m):
		maxh = max([row[i] for row in a])
		for j in range(n):
			b[j][i] = min(b[j][i], maxh)

	YES = True
	for i in range(n):
		for j in range(m):
			if a[i][j] != b[i][j]:
				YES = False
	
	fout.write('Case #%d: %s\n' % (t + 1, 'YES' if YES else 'NO'))
	
