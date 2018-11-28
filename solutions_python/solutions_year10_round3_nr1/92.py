class MyWire:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def getA(self):
		return self.a

	def getB(self):
		return self.b


def getIntersectionCnt(wireCnt, wires):
	wires.sort(key=lambda k: k.getA())
	cnt = 0
	for i in range(wireCnt):
		wire1 = wires[i]
		for j in range(i+1, wireCnt):
			wire2 = wires[j]
			if wire1.getB() > wire2.getB():
				cnt = cnt + 1
	return cnt


import sys

fileNamePrefix = sys.argv[1]
fileNameIn = fileNamePrefix + ".in"
fileNameOut = fileNamePrefix + ".out"

fileIn = open(fileNameIn, 'r')
lines = fileIn.readlines()

testcnt = int(lines[0])
idx = 1

fileOut = open(fileNameOut, 'w')

for test in range(testcnt):
	line = lines[idx].split(' ')
	idx += 1
	wireCnt = int(line[0])

	wires = []
	for i in range(wireCnt):
		line = lines[idx].split(' ')
		idx += 1
		wires.append( MyWire( int(line[0]), int(line[1]) ) )

	res = getIntersectionCnt(wireCnt, wires)

	fileOut.write("Case #{0}: {1}\n".format(test + 1, res))
