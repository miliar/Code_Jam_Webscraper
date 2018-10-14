import sys

data = sys.stdin.readlines()
counter = 0
numTests = int(data[counter])
counter += 1

for i in xrange(numTests):
	curData = data[counter].split()
	counter += 1

	C = float(curData[0])
	F = float(curData[1])
	X = float(curData[2])

	rate = 2
	numFarms = 0
	waste = 0

	best = X / rate

	while(1):
		numFarms += 1
		waste += C / rate
		rate += F
		curBest = X / rate + waste
		if curBest < best:
			best = curBest
		else:
			break

	print "Case #%d: %.7f" % ((i+1), best)
