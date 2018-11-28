#!/bin/py
import re
t = int(raw_input().strip())
for plan in range(t):
	y, x = [int(dimension.strip()) for dimension in raw_input().strip().split()]
	grid = []
	for _ in range(y):
		row = [int(tile.strip()) for tile in raw_input().strip().split()]
		grid.append(row) # should be length x
	
	problem = False
	for row in range(y):
		if not problem:
			for col in range(x):
				if not problem and \
				 ((max([grid[y_offset][col] for y_offset in range(y)]) > grid[row][col] and \
				   max([grid[row][x_offset] for x_offset in range(x)]) > grid[row][col] ) or \
				   grid[row][col] > 100):
					problem = True
	
	if problem:
		print "Case #{0}: NO".format(plan + 1)
	else:
		print "Case #{0}: YES".format(plan + 1)

