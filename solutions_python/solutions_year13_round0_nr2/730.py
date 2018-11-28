# B.py
import sys
num_cases = int(sys.stdin.readline())

for case in range(num_cases):
	size = sys.stdin.readline()
	rows = int(size.split()[0])
	columns = int(size.split()[1])

	yard = []
	for r in range(rows):
		yard.append(sys.stdin.readline())

	for r in range(rows):
		yard[r] = yard[r].split()
		yard[r] = [int(x) for x in yard[r]]

	possible = True
	for r in range(rows):
		for c in range(columns):
			# for each element it has to be tied for the biggest on its row OR column
			el = yard[r][c]
			biggest_in_col = True
			for z in range(rows):
				if yard[z][c] > el:
					biggest_in_col = False
			biggest_in_row = True
			for z in range(columns):
				if yard[r][z] > el:
					biggest_in_row = False
			if not biggest_in_row and not biggest_in_col:
				possible = False

	if possible:
		print "Case #%d: YES" % (case+1)
	else:
		print "Case #%d: NO" % (case+1)



