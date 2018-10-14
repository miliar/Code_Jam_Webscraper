def solve(mat, n):
	alphabet = set()
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			if mat[i][j] != '?' and mat[i][j] not in alphabet:
				grow(mat, i, j)
				alphabet.add(mat[i][j])
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			if mat[i][j] == '?':
				print(n+1)
	return '\n'.join([''] + [''.join(row) for row in mat])

def grow(mat, x, y):
	l, r = y, y
	while True:
		if l == 0 or mat[x][l-1] not in (mat[x][y],'?'):
			break
		l -= 1
	while True:
		if r == len(mat[x]) - 1 or mat[x][r+1] not in (mat[x][y],'?'):
			break
		r += 1
	
	t, b = x, x
	while True:
		if t == 0:
			break
		tcheck = [0 if c in (mat[x][y],'?') else 1 for c in mat[t - 1][l : r+1]]
		if sum(tcheck) > 0:
			break
		t -= 1
	while True:
		if b == len(mat) - 1:
			break
		bcheck = [0 if c in (mat[x][y],'?') else 1 for c in mat[b + 1][l : r+1]]
		if sum(bcheck) > 0:
			break
		b += 1
	
	for i in range(t, b+1):
		for j in range(l, r+1):
			mat[i][j] = mat[x][y]

def getInputFromFile(filename):
	f = open(filename, 'rt')
	n = int(f.readline().rstrip())
	inputs = []
	for i in range(n):
		r,c = f.readline().rstrip().split(' ')
		mat = []
		for j in range(int(r)):
			mat.append(list(f.readline().rstrip()))
		inputs.append(mat)
	f.close()
	return n, inputs	
	
	
def getAns(filename, outputFile):
	n, inputs = getInputFromFile(filename)
	res = []
	for i in range(n):
		ans = solve(inputs[i], i)
		res.append('Case #{}: {}'.format(i+1, ans))
	f = open(outputFile, 'wt')
	s = '\n'.join(res) + '\n'
	#print(s)
	f.write(s)
	f.close()