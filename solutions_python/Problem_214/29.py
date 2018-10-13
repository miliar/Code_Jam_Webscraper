getline = lambda: [int(x) for x in raw_input().split()]

from collections import defaultdict
impossible = "IMPOSSIBLE"

def coordinates(R,C):
	return [(i,j) for i in range(R) for j in range(C)]

def between(a,b):
	a,b = sorted([a,b])
	return range(a+1,b)

def update(d, grid, empty_spaces):
	shot_at = defaultdict(list)
	for r,c in empty_spaces:
		for r1, c1 in d:
			if r == r1 and '-' in d[(r1,c1)] and all(grid[r][i] != '#' for i in between(c, c1)):
				shot_at[(r,c)].append(('-', (r1,c1)))
			if c == c1 and '|' in d[(r1,c1)] and all(grid[i][c] != '#' for i in between(r, r1)):
				shot_at[(r,c)].append(('|', (r1,c1)))
		if len(shot_at[(r,c)]) == 1:
			[(laser, (r1,c1))] = shot_at[(r,c)]
			d[(r1,c1)] = [x for x in d[(r1,c1)] if x == laser]
		if len(shot_at[(r,c)]) == 0:
			return None
	return d

def find_answer(d, grid, empty_spaces):
	update_d = update(d, grid, empty_spaces)
	if not update_d:
		return None
	if update_d != d:
		return find_answer(update_d, grid, empty_spaces)
	for (r1,c1) in d:
		if len(d[(r1,c1)]) == 2:
			d[(r1,c1)] = ['-']
			ok = find_answer(d, grid, empty_spaces)
			if ok: return ok
			d[(r1,c1)] = ['|']
			ok  = find_answer(d, grid, empty_spaces)
			if ok: return ok
			return None
		if len(d[(r1,c1)]) == 0:
			return None
	return d

T = int(raw_input())
for test_case in range(T):
	R, C = getline()
	grid = [list(raw_input()) for _ in range(R)]
	d = {}
	empty_spaces = []
	for r,c in coordinates(R,C):
		if grid[r][c] in '-|':
			d[(r,c)] = ['-','|']
		if grid[r][c] == '.':
			empty_spaces.append((r,c))
	for r1, c1 in d:
		for r2, c2 in d:
			if (r1,c1) == (r2, c2): continue
			if r1 == r2:
				if all(grid[r1][i] != '#' for i in between(c1, c2)):
					if '-' in d[(r1,c1)]:
						d[(r1, c1)].remove('-')
					if '-' in d[(r2,c2)]:
						d[(r2, c2)].remove('-')
			if c1 == c2:
				if all(grid[i][c1] != '#' for i in between(r1, r2)):
					if '|' in d[(r1,c1)]:
						d[(r1,c1)].remove('|')
					if '|' in d[(r2,c2)]:
						d[(r2,c2)].remove('|')
	d = find_answer(d, grid, empty_spaces)
	#print "INPUT #%s"%(test_case+1)
	#print '\n'.join([''.join(x) for x in grid])
	if not d or any(not d[x] for x in d):
		answer = impossible
	else:
		possible = "POSSIBLE\n"
		for r,c in coordinates(R,C):
			if (r,c) in d:
				grid[r][c] = d[(r,c)][0]
		solution = '\n'.join([''.join(x) for x in grid])
		answer = possible + solution
	print "Case #%s: %s"%(test_case+1, answer)
