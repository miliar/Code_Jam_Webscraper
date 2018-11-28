#!/usr/bim/env python

import sys,copy

def fill_loc(grid,mapping,i,j):
	grid[i][j] = '.'
	rows = len(grid)
	cols = len(grid[0])
	for k in [-1,0,1]:
		r = i + k
		if r < 0 or r >= rows:
			continue
		else:	
			for h in [-1,0,1]:
				c = j + h
				if  c < 0 or c >= cols:
					continue
				else:
					mapping[i+k][j+h] -= 1
	mapping[i][j] += 1
	return grid,mapping

def fill_adj(grid,mapping,i,j):
	rows = len(grid)
	cols = len(grid[0])
	for k in [-1,0,1]:
		r = i + k
		if r < 0 or r >= rows:
			continue
		else:	
			for h in [-1,0,1]:
				c = j + h
				if  c < 0 or c >= cols:
					continue
				else:
					if grid[r][c] != '.':
						grid,mapping = fill_loc(grid,mapping,r,c)
	return grid,mapping

def flood_fill(grid,mapping,empty):
	empty_count = sum([ z == '.' for x in grid for z in x])

#	print '\n'.join( [''.join(row) for row in grid] ),'\n'

	if empty_count == empty:
		return grid, mapping,1
	if empty_count > empty:
		return [],[],0

	empties = []
	scores = []
	for j in range(len(grid)):
		for k in range(len(grid[0])):
			if grid[j][k] == '.' and mapping[j][k] != 0:
				empties.append( (j,k) )
				scores.append( mapping[j][k] )

#	best_score = min(scores)
#	best_locs = [ x for x,y in zip(empties,scores) if y == best_score]
	best_locs = [x for x,y in zip(empties,scores)]

	for loc in best_locs:

		grid_copy = copy.deepcopy(grid)
		map_copy = copy.deepcopy(mapping)
		grid_copy,map_copy = fill_adj(grid_copy,map_copy,loc[0],loc[1])

		grid_copy,map_copy,flag = flood_fill(grid_copy,map_copy,empty)
		if flag:
			break
	if flag:
		return grid_copy,map_copy,1
	else:
		return [],[],0
	
f = open(sys.argv[1])
g = open(sys.argv[1]+'.output','w')
n = int(f.readline().strip())
for i in xrange(n):
	line = [int(j) for j in f.readline().strip().split()]

	row = line[0]
	col = line[1]
	mines = line[2]
	empty = row * col - mines

	grid = [['*']*col for k in range(row)]

	mapping = [[8]*col for k in range(row)]
	for j in range(row):
		mapping[j][0] -= 3
		mapping[j][-1] -= 3
	for j in range(col):
		mapping[0][j] -= 3
		mapping[-1][j] -= 3
	mapping[0][0] += 1
	mapping[0][-1] += 1
	mapping[-1][0] += 1
	mapping[-1][-1] += 1
	if col == 1 or row  == 1:
		mapping[0][0] =  1
		mapping[-1][-1] = 1

	#set corner to empty
	grid,mapping = fill_loc(grid,mapping,0,0)

	#flood fill
	grid,mapping,flag = flood_fill(grid,mapping,empty)

	output = "Case #"+str(i+1)+':\n'
	if flag:
		grid[0][0] = 'c'
		output += '\n'.join( [''.join(x) for x in grid] )
	else:
		output += 'Impossible'
	print output,'\n',row,col,mines,empty
	output += '\n'
	g.write(output)
	
		

	


