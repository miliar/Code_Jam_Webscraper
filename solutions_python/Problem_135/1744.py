def getGrid(f):
	grid = []
	for i in range(4):
		grid.append(set(map(int, f.readline().split(" "))))

	return grid



f = open("a-in.in")

for problem in range(int(f.readline())):
	a1 = int(f.readline())
	grid1 = getGrid(f)
	a2 = int(f.readline())
	grid2 = getGrid(f)
	match = grid1[a1-1] & grid2[a2-1]

	if len(match) == 1:
		print "Case #%d: %d" % (problem+1, list(match)[0])
	elif len(match) > 1:
		print "Case #%d: Bad magician!" % (problem+1)
	else:
		print "Case #%d: Volunteer cheated!" % (problem+1)