import sys
import itertools


#filename = "test.in"
filename = None

def boolean_str(b):
	return 'T' if b else 'F'
def print_mask(n, grid):
	for i in range(n):
		for j in range(n):
			print boolean_str(grid[i][j]),
		print

def print_grid(n, grid):
	for i in range(n):
		for j in range(n):
			print grid[i][j],
		print

def make_grid(n, models):
	grid  = [["." for i in range(n)] for i in range(n)]
	xmask = [[True for i in range(n)] for i in range(n)]
	plusmask = [[True for i in range(n)] for i in range(n)]
	place_function = {
		"+" : place_plus,
		"x" : place_x,
		"o" : place_o
	}
	for model in models:
		t, x, y = model
		place_function[t](grid,xmask, plusmask, x, y, n)
	return grid, xmask, plusmask

def diagonal_indexes(i0,j0,n):
	diag1= [(i, i0+j0-i) for i in range(n) if i0+j0-i >= 0 and i0+j0-i < n]  
	diag2= [(i0-j0+j, j) for j in range(n) if i0-j0+j >= 0 and i0-j0+j < n]
	return diag1 + diag2

def row_column_indexes(i, j, n):
	row = [(ii,j) for ii in range(n)]
	column = [(i, jj) for  jj in range(n)]
	return row + column

def place_plus(grid, xmask, plusmask, i, j, n):
	if grid[i][j] == ".":
		grid[i][j] = "+"
	elif grid[i][j] == "x":
		grid[i][j] = "o"

	for ii,jj in diagonal_indexes(i,j, n): plusmask[ii][jj] = False

def place_x(grid, xmask, plusmask, i, j, n):
	if grid[i][j] == ".":
		grid[i][j] = "x"
	elif grid[i][j] == "+":
		grid[i][j] = "o"
		
	for ii,jj in row_column_indexes(i,j, n): xmask[ii][jj] = False

def place_o(grid, xmask, plusmask, i, j, n) :
	place_x(grid, xmask, plusmask, i, j, n)
	place_plus(grid, xmask, plusmask, i, j, n)

def remember(i,j, t, memory):
	key = (i,j)
	if key in memory.keys():
		if t != memory[key]:
			memory[key] = "o"
	else:
		memory[key] = t

def style_points(grid,n):
	model_styles = {
		"+" : 1,
		"x" : 1,
		"o" : 2,
		"." : 0
	}
	return sum([model_styles[grid[i][j]] for i in range(n) for j in range(n)])


def solve(casenum, n, m, models):
	grid, xmask, plusmask = make_grid(n, models)
	placed_stuff= {}
	for i in range(n):
		for j in range(n):
			if xmask[i][j]:
				place_x(grid, xmask,plusmask, i, j, n)
				remember(i,j, "x", placed_stuff)
	for k in range(n/2+1):
		for j in range(k, n-k):
			indices = set([(k,j), (n-1-j, k), (n-k-1, j), (n-j-1, n-k-1)])
			for ii,jj in indices: 
				if plusmask[ii][jj]:
					place_plus(grid, xmask,plusmask, ii,jj,n)
					remember(ii,jj,"+", placed_stuff)


	points = style_points(grid,n)
	print "Case #%d: %d %d" % (casenum+1, points, len(placed_stuff.keys()))
	for coords, t in placed_stuff.items():
		x, y = coords[0]+1, coords[1]+1
		print grid[x-1][y-1], x, y
		
def main():
	if filename:
		file = open(filename)
	else:
		file = sys.stdin


	T = int(file.readline().strip())
	for case in range(T):
		models =[]
		N, M = map(int, file.readline().strip().split())
		for i in range(M):
			t, x, y = file.readline().strip().split()
			models.append((t, int(x)-1, int(y)-1))
		
		solve(case, N, M, models)
		

	if file is not sys.stdin:
	    file.close()


if __name__ == '__main__':
	main()
