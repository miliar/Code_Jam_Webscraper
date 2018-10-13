import psyco
import math
import sys

INPUT_FILENAME = "C-large"

sample = file("%s.in" % INPUT_FILENAME, "rb")
output = file("%s.out" % INPUT_FILENAME, "wb")

psyco.full()

def toOutput(line):
	print line
	output.write("%s\n" % line)

def solve(caseNumber, candies):
	if reduce(lambda x, y: x ^ y, candies):
		toOutput("Case #%d: NO" % caseNumber)
		return

	toOutput("Case #%d: %d" % (caseNumber, sum(candies) - min(candies)))

numberOfTestCases = int(sample.readline())
for i in xrange(1, numberOfTestCases + 1):
	N = int(sample.readline())
	candies = map(int, sample.readline().split())
		
	solve(i, candies)