import psyco
import math
import sys

INPUT_FILENAME = "D-large"

sample = file("%s.in" % INPUT_FILENAME, "rb")
output = file("%s.out" % INPUT_FILENAME, "wb")

psyco.full()

def toOutput(line):
	print line
	output.write("%s\n" % line)

def solve(caseNumber, nums):
	expected = 0

	for i in xrange(len(nums)):
		if nums[i] != i + 1:
			expected += 1

	toOutput("Case #%d: %.6f" % (caseNumber, expected))

numberOfTestCases = int(sample.readline())
for i in xrange(1, numberOfTestCases + 1):
	N = int(sample.readline())
	nums = map(int, sample.readline().strip().split())

	solve(i, nums)
