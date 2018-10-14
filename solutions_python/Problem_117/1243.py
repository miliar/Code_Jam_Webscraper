def solve(garden, size):
	(m, i, j) = findmin(garden)
	if checkRow(garden, i, m):
		for r in range(i+1, size[0]):
			garden[r-1] = garden[r]
		garden.pop()
		size[0] = size[0]-1
		if (size[0]==0):
			return "YES"
		return solve(garden, size)
	elif checkCol(garden, j, m):
		for r in range(size[0]):
			for c in range(j+1, size[1]):
				garden[r][c-1] = garden[r][c]
			garden[r].pop()
		size[1] = size[1]-1
		if (size[1]==0):
			return "YES"
		return solve(garden, size)
	
	return "NO"
	
def findmin(garden):
	result = [100,-1,-1]
	for r in range(len(garden)):
		row = garden[r]
		for c in range(len(row)):
			if (row[c] < result[0]):
				result[0] = row[c]
				result[1] = r
				result[2] = c
	return result

def checkRow(garden, r, m):
	for i in range(len(garden[r])):
		if garden[r][i]!=m:
			return False
	return True

def checkCol(garden, c, m):
	for j in range(len(garden)):
		if garden[j][c] != m:
			return False
	return True

import sys
infile = open(sys.argv[1], 'r')
n = int(infile.readline().strip())
for i in range(n):
	size = [int(t) for t in infile.readline().strip().split()]
	garden = []
	for r in range(size[0]):
		garden.append([int(t) for t in infile.readline().strip().split()])
	print("Case #" + str(i+1) + ": " + str(solve(garden, size)))
