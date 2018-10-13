from collections import deque

def process(f):
	# Read relevant info
	numBlocks = int(f.readline())
	naomiBlocks = [float(x) for x in f.readline().split(' ')]
	kenBlocks = [float(x) for x in f.readline().split(' ')]
	naomiBlocks.sort()
	kenBlocks.sort()

	cheatingPoints = 0
	normalPoints = 0

	# First calculate the points when playing War
	kenIndex = numBlocks - 1
	for naomiIndex in reversed(range(numBlocks)):
		if naomiBlocks[naomiIndex] > kenBlocks[kenIndex]:
			normalPoints = normalPoints + 1
		else:
			kenIndex = kenIndex - 1

	# Calculate points when playing Cheating War
	kenIndex = 0
	for naomiIndex in range(numBlocks):
		if naomiBlocks[naomiIndex] > kenBlocks[kenIndex]:
			cheatingPoints = cheatingPoints + 1
			kenIndex = kenIndex + 1

	return cheatingPoints, normalPoints

with open("testcase") as f:
	numCases = int(f.readline())
	for case in range(1, numCases + 1):
		cheating, normal = process(f)
		print "Case #{case}: {cheating} {normal}".format(case=case, cheating=cheating, normal=normal)