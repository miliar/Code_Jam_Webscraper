import sys
import numpy as np
import heapq


def rectOk(r1,c1,r2,c2,skip,grid):
	for r in range(r1,r2+1):
		for c in range(c1,c2+1):
			if grid[r][c] != '?' and grid[r][c] != skip:
				return False
	return True

def solve(R,C,grid):
	processed = set()
	for r in range(R):
		for c in range(C):
			current = grid[r][c]
			if current == '?' or current in processed:
				continue
			
			processed.add(current)
			maxRect = (r,c,r,c)
			maxArea = 1


			for r1 in range(0,r+1):
				for r2 in range(r,R):
					for c1 in range(0,c+1):
						for c2 in range(c,C):
							area = (r2-r1+1)*(c2-c1+1)
							if area > maxArea:
								if rectOk(r1,c1,r2,c2,current,grid):
									maxArea = area
									maxRect = (r1,c1,r2,c2)

			r1,c1,r2,c2 = maxRect
			for rp in range(r1,r2+1):
				for cp in range(c1,c2+1):
					grid[rp][cp] = current


	return grid


t = int(raw_input())
for i in range(1, t + 1):

	R, C = [int(s) for s in raw_input().split(" ")]
	grid = []
	for r in range(R):
		grid.append([c for c in raw_input()])

	
	result = solve(R, C, grid)

	print("Case #{}:".format(i))
	for el in result:
		print("{}".format("".join(el)))
