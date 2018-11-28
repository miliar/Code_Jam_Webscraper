import sys


t = input()
for i in range(0, t):
	case = raw_input()
	s = case.split(" ")
	r = int(s[0])
	c = int(s[1])
	grid = []
	for j in range(0, r):
		s = raw_input()
		row = []
		for k in range(0, len(s)):
			row.append(s[k])
		grid.append(row)

	for j in range(0, r):
		row = grid[j]
		for k in range(1, len(row)):
			if row[k] == '?':
				row[k] = row[k-1]

		for k in range(len(row)-2, -1, -1):
			if row[k] == '?':
				row[k] = row[k+1]

	for j in range(1, r):
		row = grid[j]
		for k in range(0, len(row)):
			if row[k] == '?':
				grid[j] = grid[j-1]

	for j in range(r-2, -1, -1):
		row = grid[j]
		for k in range(0, len(row)):
			if row[k] == '?':
				grid[j] = grid[j+1]

	print "Case #"+`i+1`+": "
	for j in range(0, r):
		row = grid[j]
		res = ""
		for k in range(0, len(row)):
			res = res+row[k]
		print res

