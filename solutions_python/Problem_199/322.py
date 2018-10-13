
def solve(pancakes, flipperSize):
	# print pancakes, flipperSize
	flipperSize = int(flipperSize)

	flipped = [1 if c == '-' else 0 for c in pancakes]
	numFlipped = 0
	for i in xrange(len(pancakes) - flipperSize + 1):
		if flipped[i] % 2 == 0:
			continue

		numFlipped = numFlipped + 1
		for j in xrange(flipperSize):
			flipped[i+j] = flipped[i+j] + 1

	if len([f for f in flipped[-flipperSize:] if f % 2 != 0]) != 0:
		return -1

	return numFlipped

cases = int(input())

for i in xrange(cases):
	numFlipped = solve(*raw_input().split(' '))
	if numFlipped < 0:
		print "Case #%d: IMPOSSIBLE" % (i+1)
	else:
		print "Case #%d: %d" % ((i+1), numFlipped)
