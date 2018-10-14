import re
import sys
import math

inp = open("in.txt")
out = open("out.txt","w+")


def solve():
	cases = int(inp.readline())
	for case in xrange(cases):
		rows, cols = [int(x) for x in inp.readline().split()]
		if rows == 1 or cols == 1:
			write_case(case + 1, "YES")
			for i in xrange(rows):
				inp.readline()
			continue
		
		max_row = {}
		max_col = {}
		grid = []
		
		for i in xrange(rows):
			row = [int(x) for x in inp.readline().split()]
			grid.append(row)
			max_row[i] = max(row)
			for j in xrange(cols):
				max_col[j] = max(max_col.setdefault(j, 0), row[j])
		stopped = False
		for row in xrange(rows):
			for col in xrange(cols):
				value = grid[row][col]
				if value not in [max_row[row], max_col[col]]:
					stopped = True
					break
			if stopped:
				write_case(case + 1, "NO")
				break
		if not stopped:
			write_case(case + 1, "YES" )
		

def write_case(case, *args):
	print "printing case", case, args
	out.write("Case #%s: %s\n" % (case, " ".join([str(a) for a in args])))
	
solve()