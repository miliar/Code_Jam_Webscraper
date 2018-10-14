def readGrid(input):
	grid = []
	for line in xrange(0, 4):
		cards = [int(x) for x in input.readline().split(" ")]
		grid.append(cards)
	return grid

input = open("small.in", "r")
tests = int(input.readline())

for test in xrange(1, tests + 1):
	guess_one = int(input.readline())
	grid_one = readGrid(input)
	guess_two = int(input.readline())
	grid_two = readGrid(input)

	result = list(set(grid_one[guess_one - 1]) & set(grid_two[guess_two - 1]))
	output = ""
	if result == []:
		output = "Volunteer cheated!"
	elif len(result) > 1:
		output = "Bad magician!"
	else:
		output = str(result[0])
	print "Case #%d: %s" % (test, output)
