#!/usr/bin/python


def readfile():
	res = []
	with open('models.in', 'r') as f:
		t = int(f.readline())
		for i in xrange(t):
			n, m = map(int, f.readline().split())
			A = [['.' for _ in xrange(n)] for _ in xrange(n)]
			for _ in xrange(m):
				char, x, y = f.readline().split()
				x = int(x)
				y = int(y)
				A[x-1][y-1] = char
			testcase = solve(A)
			res.append(testcase)		
	return res


def solve(A):
	zero = 0
	z = 0
	res = []
	if 'o' in A[0]:
		zero = A[0].index('o')
	elif 'x' in A[0]:
		zero = A[0].index('x')
		z += 1
		A[0][zero] = 'o'
		res.append(('o', 0, zero))
	else:
		A[0][zero] = 'o'
		z += 1
		res.append(('o', 0, zero))
	
	for i in xrange(len(A)):
		if A[0][i] != 'o' and A[0][i] != '+':
			A[0][i] = '+'
			z += 1
			res.append(('+', 0, i))
		
	for i in xrange(1, len(A) - 1):
		A[len(A)-1][i] = '+'
		z += 1
		res.append(('+', len(A) - 1, i))
		
	for i in xrange(len(A)-1, 0, -1):
		if i != zero:
			A[i][i] = 'x'
			z += 1
			res.append(('x', i, i))
			
	if zero != 0:
		A[zero][0] = 'x'
		z += 1
		res.append(('x', zero, 0))
	
	maxscore = 3*len(A)-2 if len(A) > 1 else 2
	return z, maxscore, res


res = readfile()
with open('moderls.out', 'w') as f:
    for i, sol in enumerate(res):
		f.write('Case #%d: %d %d\n' % (i+1, sol[1], sol[0]))
		for s in sol[2]:
			f.write('%s %d %d\n' % (s[0], s[1] + 1, s[2] + 1))