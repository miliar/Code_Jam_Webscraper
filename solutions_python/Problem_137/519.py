import copy
grid = []
test = []
used = []
r = 0
c = 0
m = 0
ck = 0

def dfs(i,j):
	global test, used, r, c
	if (i < 0 or i >= r or j < 0 or j >= c or used[i][j] == 1): return 0
	used[i][j] = 1
	if test[i][j] == '1': return 1
	su = 1
	for x in range(i-1, i+2):
		for y in range(j-1, j+2):
			if x == i and y == j: continue
			su += dfs(x, y)
	return su
			
def check():
	global used, test, grid, r,c,m, ck
	ck += 1
	mines = 0
	for i in range(r):
		for j in range(c):
			if grid[i][j] == '*':
				mines += 1
	if mines != m: return False
	test = copy.deepcopy(grid)
	for i in range(r):
		for j in range(c):
			if test[i][j] == '*':
				for x in range(i-1,i+2):
					if x < 0 or x >= r: continue
					for y in range(j-1, j+2):
						if y < 0 or y >= c: continue
						if test[x][y] == '.': test[x][y] = '1'
	for i in range(r):
		for j in range(c):
			if test[i][j] != '*':
				used = [[0 for k in range(c)] for l in range(r)]
				df = dfs(i, j)
				if (df == r*c - m): 
					grid[i][j] = 'c'
					return True
	if ck > 7000: return True
	return False 

def rec(i, j, n):
	global grid,c,r,m
	if i >= c:
		ret = rec(0,j+1, n)
		return ret
	if j >= r:
		return check()
	if (n < m):
		grid[j][i] = '*'
		if rec(i+1, j, n+1): return True
	grid[j][i] = '.'
	if rec(i+1, j, n): return True
	return False
	

T = int(raw_input())

for t in range(1,T+1):
	line = raw_input().split()
	r = int(line[0])
	c = int(line[1])
	m = int(line[2])
	grid = [['.' for i in range(c)] for j in range(r)]
	print "Case #%d:"%(t)
	ck = 0
	if (not rec(0,0, 0)) or ck > 7000:
		print "Impossible"
	else:
		for line in grid:
			st = ''
			for char in line:
				st += char
			print st
			
		
	
	
