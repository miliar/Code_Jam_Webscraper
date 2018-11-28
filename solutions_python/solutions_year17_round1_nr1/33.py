#!/usr/local/bin/python3

getl = lambda: input().strip()
get = lambda: tuple(map(int, getl().split()))

def memo(f):
	cache = dict()
	def wrap(*args):
		if args not in cache: cache[args] = f(*args)
		return cache[args]
	return wrap

def solve(R, C, y):
	x = [[None] * C for r in range(R)]
	for r in range(R):
		for c in range(C):
			if y[r][c] != '?':
				z = y[r][c]
				x[r][c] = z
				r0 = r + 1
				while r0 < R and y[r0][c] == '?':
					x[r0][c] = z
					r0 += 1

	for c in range(C):
		if all(x[r][c] is None for r in range(R)):
			if c > 0:
				for r in range(R):
					x[r][c] = x[r][c-1]
		elif any(x[r][c] is None for r in range(R)):
			z = None
			for r in reversed(list(range(R))):
				if x[r][c] is not None:
					z = x[r][c]
				else:
					x[r][c] = z

	for c in reversed(list(range(C))):
		if x[0][c] is None:
			for r in range(R):
				x[r][c] = x[r][c+1]

	if any(None in l for l in x):
		print(x)
	return x

testCases, = get()
for testCase in range(1, testCases + 1):
	R, C = get()
	y = [getl() for r in range(R)]
	print('Case #{}:\n{}'.format(testCase, '\n'.join(''.join(l) for l in solve(R, C, y))))
