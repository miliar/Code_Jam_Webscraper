import psyco
import sys

INPUT_FILENAME = "C-small-attempt0"

sample = file("%s.in" % INPUT_FILENAME, "rb")
output = file("%s.out" % INPUT_FILENAME, "wb")

psyco.full()

def toOutput(line):
	print line
	output.write("%s\n" % line)

def createCache(caseNumber, n):
	result = 0

	for i in xrange(2**(n - 1)):
		l = []
		for j in xrange(n):
			if (i >> j) & 0x1:
				l.append(j + 2)
		
		if n not in l:
			continue
		
		current = n
		good = True
		while current != 1:
			greater = len([a for a in l if a <= current])
			if greater in l or greater == 1:
				current = greater
			else:
				good = False
				break
		
		if good:
			result += 1
	
	return result % 100003

def solve(caseNumber, n):
	toOutput("Case #%d: %s" % (caseNumber, resultCache[n - 2]))

numberOfTestCases = int(sample.readline())
resultCache = [1, 2, 3, 5, 8, 14, 24, 43, 77, 140, 256, 472, 874, 1628, 3045, 5719, 10780, 20388, 38674, 73562, 40265, 68060, 13335, 84884]

for i in xrange(numberOfTestCases):
	n = int(sample.readline())

	solve(i + 1, n)