
from copy import copy
from collections import defaultdict

def print_grid(grid,R,C):
	s = ''
	for y in xrange(R):
		for x in xrange(C):
			s += grid[(x,y)]
		s += '\n'
	return s[:-1]

def neighbors(R,C,x,y):
	n = []
	if y>0:
		n.append((x,y-1))
		if x<C-1:
			n.append((x+1,y-1))
		if x>0:
			n.append((x-1,y-1))
	if x>0:
		n.append((x-1, y))
	if x<C-1:
		n.append((x+1, y))
	if y<R-1:
		n.append((x,y+1))
		if x<C-1:
			n.append((x+1,y+1))
		if x>0:
			n.append((x-1,y+1))
	return n

def init_state(x,y):
	return {
		'opened': set([(x,y)]),
		'zeros': set(),
		'stack': [(x,y)],
		'click': (x,y)
	}

def solve(R,C,M):
	opens = R*C-M
	grid = defaultdict(lambda: '*')
	states = []
	#for x in xrange(C):
	#	for y in xrange(R):
	#		states.append(init_state(x,y))
	states.append(init_state(C-1,R-1))
	while states:
		state = states.pop()
		opened = state['opened']
		zeros = state['zeros']
		stack = state['stack']
		click = state['click']
		while stack:
			cell = stack.pop()
			if cell in zeros:
				for n in sorted(neighbors(R,C,cell[0],cell[1]), reverse=True):
					if n not in opened:
						stack.append(n)
						opened.add(n)
			else:
				if len(opened | set(neighbors(R,C,cell[0],cell[1])))<=opens:
					states.append({
						'opened': copy(opened),
						'zeros': copy(zeros),
						'stack': copy(stack),
						'click': click
					})
					zeros.add(cell)
					stack.append(cell)

		if (opens==1 or len(zeros)>0) and len(opened)==opens:
			break

	if not ((opens==1 or len(zeros)>0) and len(opened)==opens):
		print 'Impossible'
		return

	for n in opened:
		grid[n] = '.'
	grid[click] = 'c'
	print print_grid(grid, R, C)

T = int(raw_input())
for t in xrange(1,T+1):
	R, C, M = map(int, raw_input().split())
	print 'Case #%d:' % (t)
	solve(R, C, M)
