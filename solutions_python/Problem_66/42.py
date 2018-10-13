import psyco
import math
import sys

INPUT_FILENAME = "B-large"

sample = file("%s.in" % INPUT_FILENAME, "rb")
output = file("%s.out" % INPUT_FILENAME, "wb")

psyco.full()

def toOutput(line):
	print line
	output.write("%s\n" % line)

def cost(root, prices, matches):
	if [m for m in matches if m < 0]:
		return sys.maxint
	
	if len(matches) == 2:
		if matches[0] == 0 or matches[1] == 0:
			return prices[root]
		else:
			return 0

	return min(prices[root] + cost(root * 2 + 1, prices, matches[:len(matches) / 2]) + cost(root * 2 + 2, prices, matches[len(matches) / 2:]), 
	cost(root * 2 + 1, prices, [m - 1 for m in matches[:len(matches) / 2]]) + cost(root * 2 + 2, prices, [m - 1 for m in matches[len(matches) / 2:]]))

def solve(caseNumber, p, matches, prices):
	result = cost(0, prices, matches)

	toOutput("Case #%d: %s" % (caseNumber, result))

numberOfTestCases = int(sample.readline())

for i in xrange(numberOfTestCases):
	p = int(sample.readline())

	matches = [int(num) for num in sample.readline().strip().split(" ")]

	prices = []
	for j in xrange(p):
		prices.append([int(num) for num in sample.readline().strip().split(" ")])
	
	prices.reverse()
	prices = reduce(lambda a,b: a + b, prices)

	solve(i + 1, p, matches, prices)