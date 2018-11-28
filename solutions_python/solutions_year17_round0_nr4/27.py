from collections import defaultdict

gets = lambda: input().split()
get = lambda: map(int, gets())

def memo(f):
	cache = dict()
	def wrap(*args):
		if args not in cache: cache[args] = f(*args)
		return cache[args]
	return wrap



def solve(n, nodes):
	full = [[[False, False] for c in range(n)] for r in range(n)]
	requiredStraightFull = set()
	requiredDiagonalFull = set()
	rows = set()
	cols = set()
	xrows = set()
	xcols = set()

	getRow = lambda xr, xc: (xr + xc) // 2
	getCol = lambda xr, xc: (xr - xc) // 2

	xrowValues = dict()
	xcolValues = dict()
	for r in range(n):
		for c in range(n):
			if r+c not in xrowValues: xrowValues[r+c] = set()
			if r-c not in xcolValues: xcolValues[r-c] = set()
			xrowValues[r+c].add(r-c)
			xcolValues[r-c].add(r+c)


	STRAIGHT, DIAGONAL = 0, 1

	for kind, r, c in nodes:
		if kind == 'x' or kind == 'o':
			full[r][c][STRAIGHT] = True
			requiredStraightFull.add((r, c))
			rows.add(r)
			cols.add(c)
		if kind == '+' or kind == 'o':
			full[r][c][DIAGONAL] = True
			requiredDiagonalFull.add((r + c, r - c))
			xrows.add(r + c)
			xcols.add(r - c)


	def fillRow(r):
		for c in range(n):
			if c not in cols:
				full[r][c][STRAIGHT] = True
				rows.add(r)
				cols.add(c)
				return

	for r in range(n):
		if r not in rows:
			fillRow(r)
			assert r in rows

	def displayBoard():
		print('\n'.join(''.join('o' if all(full[r][c]) else 'x' if full[r][c][STRAIGHT] else '+' if full[r][c][DIAGONAL] else '.' for c in range(n)) for r in range(n)))
		print()

	def validateBoard():
		usedRows = set()
		usedCols = set()
		usedXrows = set()
		usedXcols = set()
		for r in range(n):
			for c in range(n):
				if full[r][c][STRAIGHT]:
					if r in usedRows:
						print(r, c, 'already row')
						return False
					if c in usedCols:
						print(r, c, 'already col')
						return False
					usedRows.add(r)
					usedCols.add(c)
				elif (r, c) in requiredStraightFull:
					print(r, c, 'required straight full')
					return False
				if full[r][c][DIAGONAL]:
					if r + c in usedXrows:
						print(r, c, 'already xrow')
						return False
					if r - c in usedXcols:
						print(r, c, 'already xcol')
						return False
					usedXrows.add(r + c)
					usedXcols.add(r - c)
				elif (r + c, r - c) in requiredDiagonalFull:
					print(r, c, 'required diagonal full')
					return False
		
		if usedRows != rows:
			print('usedRows != rows', usedRows, rows)
			return False
		if usedCols != cols:
			print('usedCols != cols', usedCols, cols)
			return False
		if usedXrows != xrows:
			print('usedXrows != xrows', usedXrows, xrows)
			return False
		if usedXcols != xcols:
			print('usedXcols != xcols', usedXcols, xcols)
			return False

		return True


	def augmentingPath():
		seen = set()
		def explore(state):
			if state in seen:
				return None
			seen.add(state)

			kind, info = state

			if kind == 'x':
				xr, xc = info
				if (xr, xc) in requiredDiagonalFull:
					return None
				if xr in xrows:
					path = explore(('xr', xr))
					if path is not None:
						return [('x->xr', (xr, xc))] + path
				path = explore(('xc', xc))
				if path is not None:
					return [('x->xc', (xr, xc))] + path

			elif kind == 'xr':
				xr = info
				for xc in xrowValues[xr]:
					path = explore(('x', (xr, xc)))
					if path is not None:
						return [('xr->x', (xr, xc))] + path

			elif kind == 'xc':
				xc = info
				if xc in xcols:
					for xr in xcolValues[xc]:
						if full[getRow(xr, xc)][getCol(xr, xc)][DIAGONAL]:
							path = explore(('x', (xr, xc)))
							if path is not None:
								return [('xc->x', (xr, xc))] + path
				else:
					return []

		path = None
		for xr in xrowValues:
			if xr not in xrows:
				path = explore(('xr', xr))
				if path is not None:
					break

		if path is None:
			return False

		#print(path)

		for kind, (xr, xc) in path:
			if kind == 'xr->x':
				pass
			elif kind == 'x->xr':
				pass
			elif kind == 'x->xc':
				assert (xr, xc) not in requiredDiagonalFull
				assert not full[getRow(xr, xc)][getCol(xr, xc)][DIAGONAL]
				full[getRow(xr, xc)][getCol(xr, xc)][DIAGONAL] = True
			elif kind == 'xc->x':
				assert (xr, xc) not in requiredDiagonalFull
				assert full[getRow(xr, xc)][getCol(xr, xc)][DIAGONAL]
				full[getRow(xr, xc)][getCol(xr, xc)][DIAGONAL] = False
			else:
				assert False

		kind, (xr, xc) = path[0]
		assert kind == 'xr->x'
		assert xr not in xrows
		xrows.add(xr)

		kind, (xr, xc) = path[-1]
		assert kind == 'x->xc'
		assert xc not in xcols
		xcols.add(xc)

		return True

	while augmentingPath():
		pass

	if not validateBoard():
		print()
		displayBoard()
		print()
		assert False

	assert len(rows) == n and len(cols) == n
	assert len(xrows) == len(xcols)

	return tuple(('o' if all(full[r][c]) else 'x' if full[r][c][STRAIGHT] else '+', r, c) for r in range(n) for c in range(n) if any(full[r][c]))



testCases, = get()
for testCase in range(1, testCases+1):
	
	n, m = get()
	nodes = tuple((kind, int(r) - 1, int(c) - 1) for kind, r, c in (gets() for i in range(m)))
	result = solve(n, nodes)

	for kind, r, c in result:
		if kind == '+':
			assert ('x', r, c) not in nodes and ('o', r, c) not in nodes
		if kind == 'x':
			assert ('+', r, c) not in nodes and ('o', r, c) not in nodes
		for otherKind in 'ox+':
			if otherKind != kind:
				assert (otherKind, r, c) not in result

	pointMapping = {'o': 2, 'x': 1, '+': 1}
	points = sum(pointMapping[kind] for kind, r, c in result)

	newModels = set(result) - set(nodes)

	print('Case #{}: {} {}'.format(testCase, points, len(newModels)))
	
	for kind, r, c in sorted(newModels):
		print('{} {} {}'.format(kind, r+1, c+1))
