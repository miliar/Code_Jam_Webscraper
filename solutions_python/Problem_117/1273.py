import sys

f = open(sys.argv[1], 'r')
line = f.readline().split(' ')
cases = int(line[0])

for case in range(cases):
	case = case + 1

	dims = f.readline().split(' ')
	dimX = int(dims[0])
	dimY = int(dims[1])

	grid = []
	for i in range(dimX):
		line = f.readline().rstrip().split(' ')
		row = []
		for x in line:
			row.append(int(x))
		grid.append(row)

	visited = []
	for i in range(dimX):
		visited.append([])

		for y in range(dimY):
			visited[i].append(False)

	for x in range(dimX):
		max = 0

		for y in range(dimY):
			if grid[x][y] > max:
				max = grid[x][y]

		for y in range(dimY):
			if grid[x][y] == max:
				visited[x][y] = True;

	for y in range(dimY):
		max = 0

		for x in range(dimX):
			if grid[x][y] > max:
				max = grid[x][y]

		for x in range(dimX):
			if grid[x][y] == max:
				visited[x][y] = True;

	impossible = False
	for x in range(dimX):
		for y in range(dimY):
			if visited[x][y] is False:
				impossible = True

	if impossible:
		print "Case #%i: NO" % (case)
	else:
		print "Case #%i: YES" % (case)