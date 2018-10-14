# Solution to "Lawnmower" for Google Code Jam 2013
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys
import string

with open(sys.argv[1], 'r') as f:
	numCases = int(f.readline())
	cases = []
	for _ in range(numCases):
		n,m = tuple(int(x) for x in f.readline().split())
		case = tuple(tuple(int(x) for x in f.readline().split()) for _ in range(n))
		cases.append(case)

f = open(sys.argv[2], 'w')


for c,case in enumerate(cases):
	n = len(case)
	m = len(case[0])
	row_maxes = [max(row) for row in case]
	col_maxes = [max(row[col] for row in case) for col in range(m)]
	viable = True
	for r,row in enumerate(case):
		if not viable: break
		for cx,entry in enumerate(row):
			if entry < row_maxes[r] and entry < col_maxes[cx]:
				viable = False
				break
	if viable:
		f.write("Case #%d: %s\n"%(c+1, "YES"))
	else:
		f.write("Case #%d: %s\n"%(c+1, "NO"))

f.close()