def readInput(r):
	return r.readlines()

def parseInput(r, f):
	stuff = readInput(r)
	i = 0
	count = 0
	while i < len(stuff) - 1:
		count += 1
		j = 1
		initCond = stuff[i + j].split()
		initDistance = int(initCond[0])
		extraStuff = []
		while j < int(initCond[1]) + 1:
			j += 1
			extraStuff.append(stuff[i + j].strip())
		output = businessLogic(initDistance, extraStuff)
		writeOutput(f, output, count)
		i += j


def businessLogic(initDistance, extraStuff):
	posAndSpeed = extraStuff[0].split()
	minim = (initDistance - int(posAndSpeed[0])) / int(posAndSpeed[1])
	for i in range(1, len(extraStuff)):
		posAndSpeed = extraStuff[i].split()
		tryThis = (initDistance - int(posAndSpeed[0])) / int(posAndSpeed[1])
		minim = max(minim, tryThis)
	return '%.6f' % (initDistance / minim)

def writeOutput(f, output, count):
	f.write('Case #{0}: {1}\n'.format(count, output))

def controller():
	f = open('output.txt', 'w')
	r = open('A-large.in', 'r')
	parseInput(r, f)

controller()