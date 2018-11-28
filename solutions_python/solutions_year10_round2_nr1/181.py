class DirNode:
	def __init__(self):
		self.children = {}

	def makeDir(self, path):
		newlyCreated = 0
		if path[0] not in self.children:
			self.children[path[0]] = DirNode()
			newlyCreated = 1

		if len(path) > 1:
			newlyCreated = newlyCreated + self.children[path[0]].makeDir(path[1:])

		return newlyCreated


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
	existDirCnt = int(line[0])
	newDirCnt = int(line[1])

	root = DirNode()
	for i in range(existDirCnt):
		line = lines[idx][1:-1].split('/')
		idx += 1
		root.makeDir(line)

	createCnt = 0
	for i in range(newDirCnt):
		line = lines[idx][1:-1].split('/')
		idx += 1
		createCnt = createCnt + root.makeDir(line)

	fileOut.write("Case #{0}: {1}\n".format(test + 1, createCnt))
