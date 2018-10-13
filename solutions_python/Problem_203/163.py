#!/usr/bin/python

import sys
import numpy as np

if len(sys.argv) != 2:
	print "usage: %s <input_file_name>" % sys.argv[0]
	exit()

input_file_name = sys.argv[1]
if input_file_name[-3:] == ".in":
	output_file_name = input_file_name[:-3] + ".out"
else:
	output_file_name = input_file_name + ".out"

def expand_right_bottom(grid, R, C, x, y):
	child = grid[x][y]
	bottom_most = x
	right_most = y
	for i in xrange(R):
		for j in xrange(C):
			if grid[i][j] == child:
				bottom_most = max(bottom_most, i)
				right_most = max(right_most, j)
	for i in xrange(x, bottom_most + 1):
		for j in xrange(y, right_most + 1):
			if grid[i][j] == '?':
				grid[i][j] = child
			elif grid[i][j] != child:
				print 'this should never happen'
				exit()
	for i in xrange(bottom_most + 1, R):	#try to expand downwards
		can_expand = True
		for j in xrange(y, right_most + 1):
			if grid[i][j] != child and grid[i][j] != '?':
				can_expand = False
				break
		if can_expand:
			for j in xrange(y, right_most + 1):
				if grid[i][j] == '?':
					grid[i][j] = child
				elif grid[i][j] != child:
					print 'this should never happen2'
					exit()
			bottom_most += 1
		else:
			break
	for j in xrange(right_most + 1, C):	#try to expand rightwards
		can_expand = True
		for i in xrange(x, bottom_most + 1):
			if grid[i][j] != child and grid[i][j] != '?':
				can_expand = False
				break
		if can_expand:
			for i in xrange(x, bottom_most + 1):
				if grid[i][j] == '?':
					grid[i][j] = child
				elif grid[i][j] != child:
					print 'this should never happen3'
					exit()
			right_most += 1
		else:
			break

def expand_left_top(grid, R, C, x, y):
	child = grid[x][y]
	top_most = x
	left_most = y
	for i in xrange(R):
		for j in xrange(C):
			if grid[i][j] == child:
				top_most = min(top_most, i)
				left_most = max(left_most, j)
	for i in xrange(x, top_most - 1, -1):
		for j in xrange(y, left_most - 1, -1):
			if grid[i][j] == '?':
				grid[i][j] = child
			elif grid[i][j] != child:
				print 'this should never happen(2)'
				exit()
	for i in xrange(top_most - 1, -1, -1):	#try to expand topwards
		can_expand = True
		for j in xrange(y, left_most - 1, -1):
			if grid[i][j] != child and grid[i][j] != '?':
				can_expand = False
				break
		if can_expand:
			for j in xrange(y, left_most - 1, -1):
				if grid[i][j] == '?':
					grid[i][j] = child
				elif grid[i][j] != child:
					print 'this should never happen(2)2'
					exit()
			top_most -= 1
		else:
			break
	for j in xrange(left_most - 1, -1, -1):	#try to expand leftwards
		can_expand = True
		for i in xrange(x, top_most - 1, -1):
			if grid[i][j] != child and grid[i][j] != '?':
				can_expand = False
				break
		if can_expand:
			for i in xrange(x, top_most - 1, -1):
				if grid[i][j] == '?':
					grid[i][j] = child
				elif grid[i][j] != child:
					print 'this should never happen3'
					exit()
			left_most -= 1
		else:
			break

def solve(grid, R, C):
	visited = set()
	for i in xrange(R):
		for j in xrange(C):
			if grid[i][j] != '?' and grid[i][j] not in visited:
				expand_right_bottom(grid, R, C, i, j)
				visited.add(grid[i][j])
	visited = set()
	for i in xrange(R - 1, -1, -1):
		for j in xrange(C - 1, -1, -1):
			if grid[i][j] != '?' and grid[i][j] not in visited:
				expand_left_top(grid, R, C, i, j)
				visited.add(grid[i][j])
	ret = ''
	for i in xrange(R):
		ret += '\n' + ''.join(grid[i])
	return ret

results = []
with open(input_file_name, 'r') as f:
	T = int(f.readline())
	for i in xrange(T):
		line = f.readline().strip('\n')
		R, C = [int(x) for x in line.split(' ')]
		grid = []
		for j in xrange(R):
			line = f.readline().strip('\n')
			grid.append(list(line))
		ret = solve(grid, R, C)
		results.append(ret)

with open(output_file_name, 'w') as f:
	for i in range(len(results)):
		output_string = "Case #%d: %s\n" % (i + 1, results[i])
		print output_string[:-1]
		f.write(output_string)
