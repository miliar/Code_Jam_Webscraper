import numpy as np
import pulp

def diag(n, row, drow):
	r, c = [], []
	for col in xrange(0, n):
		if 0 <= row < n:
			r.append(row)
			c.append(col)
		row += drow
	return r, c

def solve(n, reqs):
	idx = ((row, col) for row in xrange(n) for col in xrange(n))
	x = np.empty([n, n], pulp.LpVariable)
	y = np.empty([n, n], pulp.LpVariable)
	z = np.empty([n, n], pulp.LpVariable)
	for row in xrange(n):
		for col in xrange(n):
			idx = row * n + col
			x[row, col] = pulp.LpVariable('x' + str(idx), cat='Binary')
			y[row, col] = pulp.LpVariable('y' + str(idx), cat='Binary')
			z[row, col] = pulp.LpVariable('z' + str(idx), cat='Binary')
	model = pulp.LpProblem("Code Jam 2017 Qual", pulp.LpMaximize)
	model += np.sum(x) + np.sum(y) + 2 * np.sum(z)
	for row in xrange(n):
		for col in xrange(n):
			model += x[row, col] + y[row, col] + z[row, col] <= 1
	for row in xrange(n):
		model += np.sum(y[row, :]) + np.sum(z[row, :]) <= 1
		model += np.sum(y[:, row]) + np.sum(z[:, row]) <= 1
	for row in xrange(-n+1, n):
		rs, cs = diag(n, row, 1)
		model += np.sum(x[rs, cs]) + np.sum(z[rs, cs]) <= 1
	for row in xrange(0, 2 * n - 1):
		rs, cs = diag(n, row, -1)
		model += np.sum(x[rs, cs]) + np.sum(z[rs, cs]) <= 1
	cache = {}
	for req in reqs:
		ch, r, c = req.split()
		r, c = int(r) - 1, int(c) - 1
		cache[r, c] = ch
		if ch == 'o':
			model += z[r, c] == 1
		if ch == '+':
			model += x[r, c] + z[r, c] == 1
		if ch == 'x':
			model += y[r, c] + z[r, c] == 1

	model.solve()
	score = pulp.value(model.objective)
	moves = []
	for row in xrange(n):
		for col in xrange(n):
			zz = z[row, col].varValue > 0
			yy = y[row, col].varValue > 0
			xx = x[row, col].varValue > 0
			rstr = str(row + 1)
			cstr = str(col + 1)
			if xx > 0 and cache.get((row, col), '') != '+':
				moves.append(' '.join(['+', rstr, cstr]))
			if yy > 0 and cache.get((row, col), '') != 'x':
				moves.append(' '.join(['x', rstr, cstr]))
			if zz > 0 and cache.get((row, col), '') != 'o':
				moves.append(' '.join(['o', rstr, cstr]))
	return score, moves

def solve_smart(n, reqs):
	cache = {}
	board = np.full([n, n], '.')
	for req in reqs:
		ch, r, c = req.split()
		r, c = int(r) - 1, int(c) - 1
		cache[r, c] = ch
		board[r, c] = ch
	ridx = -1
	for idx in xrange(n):
		if board[0, idx] == 'x' or board[0, idx] == 'o':
			board[0, idx] = 'o'
			ridx = idx
		else:
			board[0, idx] = '+'
	if n > 1:
		board[n-1, 1:n-1] = '+'
	if ridx == -1:
		board[0, 0] = 'o'
		ridx = 0
	for idx in xrange(1, n):
		if idx != ridx:
			board[idx, idx] = 'x'
		else:
			board[idx, 0] = 'x'
	score, moves = 0, []
	for row in xrange(n):
		for col in xrange(n):
			if board[row, col] == 'o':
				score += 2
			if board[row, col] == '+':
				score += 1
			if board[row, col] == 'x':
				score += 1
			if cache.get((row, col), '.') != board[row, col]:
				moves.append('%s %s %s' % (board[row, col], row + 1, col + 1))

	return score, moves

T = int(raw_input())
for cs in xrange(T):
	n, m = (int(x) for x in raw_input().split())
	reqs = [raw_input() for _ in xrange(m)]
	score, moves = solve_smart(n, reqs)
	print 'Case #%s: %s %s' % (cs + 1, int(score), len(moves))
	for move in moves:
		print move
