#!/usr/bin/env python
import sys

def main():
	T = int(sys.stdin.readline().strip())
	for t in range(T):
		[H, W] = [int(s) for s in sys.stdin.readline().strip().split()]
		map = []
		for h in range(H):
			row = [int(s) for s in sys.stdin.readline().strip().split()]
			assert(len(row) == W)
			map.append(row)
		
		print "Case #%d:" % (t+1)
		printDrainageBasin(map, H, W)

def printDrainageBasin(map, num_rows, num_cols):
	flow = []
	for row, map_row in enumerate(map):
		flow_row = []
		for col, height in enumerate(map_row):
			best_height = height
			best_pos = (row, col)
			for drow in [-1, 0, 1]:
				for dcol in [-1, 0, 1]:
					if abs(drow) != abs(dcol):
						r = row + drow
						c = col + dcol
						if r >= 0 and r < num_rows and c >= 0 and c < num_cols:
							if map[r][c] < best_height:
								best_height = map[r][c]
								best_pos = (r, c)
			flow_row.append(best_pos)
		flow.append(flow_row)
	#printMatrix(map)
	#printMatrix(flow)
	
	order = []
	for row in range(num_rows):
		for col in range(num_cols):
			height = map[row][col]
			order.append((height, (row, col)))
	order = sorted(order, lambda (h1, p1), (h2, p2): h1-h2)
	order = [pos for (height, pos) in order]
	#print order
	
	region = -1
	regions = []
	for row in range(num_rows):
		region_row = []
		for col in range(num_cols):
			region_row.append(region)
		regions.append(region_row)

	for row, col in order:
		(frow, fcol) = flow[row][col]
		if frow == row and fcol == col:
			region += 1
			regions[row][col] = region
		else:
			regions[row][col] = regions[frow][fcol]
	
	translation = {}
	letter = ord('a')
	for row in range(num_rows):
		for col in range(num_cols):
			code = regions[row][col]
			if code not in translation:
				translation[code] = chr(letter)
				letter += 1
			regions[row][col] = translation[code]

	printMatrix(regions)
	
def printMatrix(matrix):
	for row in matrix:
		line = ''
		for col in row:
			line += str(col) + ' '
		print line.strip()

main()

