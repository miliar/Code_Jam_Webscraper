#! /usr/bin/python

import sys
import fractions

f = open(sys.argv[1], 'rt')

# HELPER FUNCTIONS FOR INPUT
def f_intlist(): return [int(x) for x in f.readline().split(' ')]
def f_strlist(): return [x.strip() for x in f.readline().split(' ')]
def f_int(): return int(f.readline())
def f_str(): return f.readline().strip()

def solve(grid, c_r, c_c, integral):
	for s in range(min(R,C), 2, -1):
		for i in range(s-1,len(grid)):
			for j in range(s-1,len(grid[0])):
				cog_r = c_r[i][j]
				cog_c = c_c[i][j]
				mass = integral[i][j]
				if i >= s:
					cog_r -= c_r[i-s][j]
					cog_c -= c_c[i-s][j]
					mass -= integral[i-s][j]
				if j >= s:
					cog_r -= c_r[i][j-s]
					cog_c -= c_c[i][j-s]
					mass -= integral[i][j-s]
				if i >= s and j >= s:
					cog_r += c_r[i-s][j-s]
					cog_c += c_c[i-s][j-s]
					mass += integral[i-s][j-s]
				cog_r -= (grid[i][j] + grid[i][j-s+1]) * i + (grid[i-s+1][j] + grid[i-s+1][j-s+1]) * (i-s+1)
				cog_c -= (grid[i][j] + grid[i-s+1][j]) * j + (grid[i][j-s+1] + grid[i-s+1][j-s+1]) * (j-s+1)
				mass -= grid[i][j] + grid[i-s+1][j] + grid[i][j-s+1] + grid[i-s+1][j-s+1]
				cog_r /= float(mass)
				cog_c /= float(mass)
				
				if abs(i - float(s-1)/2 - cog_r) < 1e-5 and abs(j - float(s-1)/2 - cog_c) < 1e-5:
					return s
	return 'IMPOSSIBLE'

for n_trial in range(1, f_int()+1):
	R, C, D = tuple(f_intlist())
	
	grid = []
	for r in range(R):
		grid.append([int(x) + D for x in f_str()])
	
	integral = [[0]*len(grid[0])]
	c_r = [[0]*len(grid[0])]
	c_c = [[0]*len(grid[0])]
	integral[0][0] = grid[0][0]
	for i in range(1,len(grid)):
		integral.append( [0]*len(grid[0]) )
		c_c.append( [0]*len(grid[0]) )
		c_r.append( [0]*len(grid[0]) )		
		integral[i][0] = integral[i-1][0] + grid[i][0]
		c_r[i][0] = c_r[i-1][0] + grid[i][0] * i
	for i in range(1,len(grid[0])):
		integral[0][i] = integral[0][i-1] + grid[0][i]
		c_c[0][i] = c_c[0][i-1] + grid[0][i] * i
	for i in range(1,len(grid)):
		for j in range(1,len(grid[0])):
			integral[i][j] = integral[i-1][j] + integral[i][j-1] - integral[i-1][j-1] + grid[i][j]
			c_r[i][j] = c_r[i-1][j] + c_r[i][j-1] - c_r[i-1][j-1] + grid[i][j] * i
			c_c[i][j] = c_c[i-1][j] + c_c[i][j-1] - c_c[i-1][j-1] + grid[i][j] * j

	
	ans = solve(grid, c_r, c_c, integral)
					 
	print "Case #%d: %s" % (n_trial, str(ans))
