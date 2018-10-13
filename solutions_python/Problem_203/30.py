#!/usr/bin/env python
from collections import defaultdict
import sys

def fill(grid, children, rs, cs, rt, ct):
	if len(children) == 1:
		for r in range(rs, rt):
			for c in range(cs, ct):
				grid[r][c] = children.keys()[0]
	else:
		a, b = sorted(children.values()[:2])
		if a[0] != b[0]:
			children_a = {c:v for c,v in children.items() if v[0] <= a[0]}
			children_b = {c:v for c,v in children.items() if v[0] > a[0]}
			fill(grid, children_a, rs, cs, a[0]+1, ct)
			fill(grid, children_b, a[0]+1, cs, rt, ct)
		else:
			children_a = {c:v for c,v in children.items() if v[1] <= a[1]}
			children_b = {c:v for c,v in children.items() if v[1] > a[1]}
			fill(grid, children_a, rs, cs, rt, a[1]+1)
			fill(grid, children_b, rs, a[1]+1, rt, ct)

if __name__ == '__main__':
	T = int(sys.stdin.readline())
	for t in range(1, T+1):
		R, C = map(int, sys.stdin.readline().strip().split())
		grid = [[c for c in sys.stdin.readline().strip()] for r in range(R)]
		children = dict()
		for r in range(R):
			for c in range(C):
				if grid[r][c] != '?':
					children[grid[r][c]] = (r,c)
		fill(grid, children, 0, 0, R, C)
		print('Case #%s:' % t)
		for row in grid:
			print(''.join(row))
