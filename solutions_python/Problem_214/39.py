from itertools import product, chain


nm = (
	(1, 3),
	(0, 2),
	(3, 1),
	(2, 0),
)
def getcoveredemptycell(r, c, d):
	covered = set()
	while True:
		if d == 0:
			c -= 1
		elif d == 1:
			r -= 1
		elif d == 2:
			c += 1
		elif d == 3:
			r += 1
		if r < 0 or r >= R:
			break
		if c < 0 or c >= C:
			break
		cell = grid[r][c]
		if cell in ('-', '|'):
			return
		if cell == '.':
			covered.add((r, c))
		elif cell == '\\':
			d = nm[d][0]
		elif cell == '/':
			d = nm[d][1]
		elif cell == '#':
			break
	return covered

for t in range(1, int(input()) + 1):
	R, C = map(int, input().split())
	grid = [list(input()) for _ in range(R)]
	l = []
	notempty = set()
	emptycount = 0
	noway = False
	for r, row in enumerate(grid):
		for c, cell in enumerate(row):
			if cell in ('-', '|'):
				try:
					covereda = getcoveredemptycell(r, c, 0) | getcoveredemptycell(r, c, 2)
				except TypeError:
					covereda = None
				try:
					coveredb = getcoveredemptycell(r, c, 1) | getcoveredemptycell(r, c, 3)
				except TypeError:
					coveredb = None
				if covereda is not None and coveredb is not None:
					l.append((r, c, (covereda, coveredb)))
				elif covereda is not None:
					notempty |= covereda
					grid[r][c] = '-'
				elif coveredb is not None:
					notempty |= coveredb
					grid[r][c] = '|'
				else:
					noway = True
					break
			elif cell == '.':
				emptycount += 1
		else:
			continue
		break

	l = [
		(r, c, (a - notempty, b - notempty))
		for r, c, (a, b) in l
	]
	l = [x for x in l if len(x[2][0]) or len(x[2][1])]
	emptycount -= len(notempty)

	if noway:
		print('Case #%d: IMPOSSIBLE' % t)
		continue

	if emptycount == 0:
		print('Case #%d: POSSIBLE' % t)
		print('\n'.join(''.join(x) for x in grid))
		continue
	for ds in product((0, 1), repeat=len(l)):
		ca = set(chain.from_iterable(ab[d] for d, (_, _, ab) in zip(ds, l)))
		if len(ca) == emptycount:
			for d, (r, c, _) in zip(ds, l):
				grid[r][c] = '-' if d == 0 else '|'
			print('Case #%d: POSSIBLE' % t)
			print('\n'.join(''.join(x) for x in grid))
			break
	else:
		print('Case #%d: IMPOSSIBLE' % t)
