import psyco
import math
import sys

INPUT_FILENAME = "C-small-attempt1"

sample = file("%s.in" % INPUT_FILENAME, "rb")
output = file("%s.out" % INPUT_FILENAME, "wb")

psyco.full()

def toOutput(line):
	print line
	output.write("%s\n" % line)

def solve(caseNumber, N, L, H, freqs):
	for j in xrange(L, H + 1):
		good = True

		for freq in freqs:
			if (j == freq) or (j > freq and j % freq == 0) or (j < freq and freq % j == 0):
				continue
			
			good = False
			break
		
		if good:
			toOutput("Case #%d: %d" % (caseNumber, j))
			return
	
	toOutput("Case #%d: NO" % caseNumber)

numberOfTestCases = int(sample.readline())
for i in xrange(1, numberOfTestCases + 1):
	N, L, H = map(int, sample.readline().split())
	freqs = map(int, sample.readline().split())

	solve(i, N, L, H, freqs)