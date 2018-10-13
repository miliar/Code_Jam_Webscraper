import sys

def time(C, F, X):
	bestTime = sys.float_info.max
	numFarms = 0
	retTime = 0.0
	while True:
		retTime = 0.0
		for i in range(numFarms):
			retTime += C / (2.0 + F * float(i))
		retTime += X / (2.0 + F * float(numFarms))
		if retTime < bestTime:
			bestTime = retTime
		else:
			return bestTime
		numFarms += 1


lines = sys.stdin.readlines()

numCases = int(lines[0])
for i in range(numCases):
	floats = [float(x) for x in lines[i+1].split()]
	print "Case #%d: %0.7f" % (i+1, time(floats[0], floats[1], floats[2]))


