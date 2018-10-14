import psyco

INPUT_FILENAME = "A-large"

sample = file("%s.in" % INPUT_FILENAME, "rb")
output = file("%s.out" % INPUT_FILENAME, "wb")

psyco.full()

def toOutput(line):
	print line
	output.write("%s\n" % line)

def solve(caseNumber, existingDirs, dirsToCreate):
	result = 0

	existingDirectories = {}

	splittedDirs = [dirname.split("/")[1:] for dirname in existingDirs]
	for i in xrange(len(splittedDirs)):
		for j in xrange(1, len(splittedDirs[i]) + 1):
			dirName = "/".join(splittedDirs[i][:j])

			existingDirectories[dirName] = 0
	
	splittedDirsToCreate = [dirname.split("/")[1:] for dirname in dirsToCreate]
	for i in xrange(len(splittedDirsToCreate)):
		for j in xrange(1, len(splittedDirsToCreate[i]) + 1):
			dirName = "/".join(splittedDirsToCreate[i][:j])

			if not existingDirectories.has_key(dirName):
				result += 1
				existingDirectories[dirName] = 0

	toOutput("Case #%d: %s" % (caseNumber, result))

numberOfTestCases = int(sample.readline())

for i in xrange(numberOfTestCases):
	numberOfDirs, numDirectoriesToCreate = [int(num) for num in sample.readline().split(" ")]

	existingDirs = []
	dirsToCreate = []

	for j in xrange(numberOfDirs):
		existingDirs.append(sample.readline().strip())
	
	for j in xrange(numDirectoriesToCreate):
		dirsToCreate.append(sample.readline().strip())

	solve(i + 1, existingDirs, dirsToCreate)