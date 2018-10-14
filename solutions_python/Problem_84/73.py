#!/usr/bin/python
#This program requires python ver 2.6 or higher. (itertools.combinations)
import sys
import itertools

#solve case function
def solve_case(row, column, tiles, case_number):
	print "Case #" + str(case_number) + ":"

	is_impossible = False
	for y in range(0, row):
		for x in range(0, column):
			if tiles[y][x] == '#':
				if x + 1 < column and y + 1 < row:
					if tiles[y][x + 1] == '#' and tiles[y + 1][x] == '#' and tiles[y + 1][x + 1] == '#':
						tiles[y][x] = '/'
						tiles[y + 1][x] = '\\'
						tiles[y][x + 1] = '\\'
						tiles[y + 1][x + 1] = '/'
					else:
						is_impossible = True
						break
				else:
					is_impossible = True
					break
		else:
			if is_impossible:
				break
	if is_impossible:
		print "Impossible"
	else:
		for line in tiles:
			print "".join(line)

#main
r = sys.stdin

if len(sys.argv) > 1:
	r = open(sys.argv[1], 'r')

total_cases = r.readline()
for case_number in range(1, int(total_cases) + 1):
	r_c = r.readline().strip().split(' ')
	row = int(r_c[0])
	column = int(r_c[1])
	tiles = []
	for n in range(0, int(row)):
		col = list(r.readline().strip())
		tiles.append(col)
	solve_case(row, column, tiles, case_number)

