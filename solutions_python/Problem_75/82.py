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

def solve(caseNumber, comb, opp, invoke):
	combNoTarget = [c[:2] for c in comb]
	eList = []

	for card in invoke:
		eList.append(card)

		if len(eList) > 1:
			possibleComb = "".join(eList[-2:])
			if possibleComb in combNoTarget:
				eList = eList[:-2] + [comb[combNoTarget.index(possibleComb)][-1]]
				continue
			elif possibleComb[::-1] in combNoTarget:
				eList = eList[:-2] + [comb[combNoTarget.index(possibleComb[::-1])][-1]]
				continue
			
			for o in opp:
				if o[0] in eList and o[1] in eList:
					eList = []

	toOutput("Case #%d: %s" % (caseNumber, "[%s]" % (", ".join(eList))))

numberOfTestCases = int(sample.readline())
for i in xrange(1, numberOfTestCases + 1):
	line = sample.readline().strip().split()
	C = int(line[0])
	comb = line[1: C + 1]
	D = int(line[C + 1])
	opp = line[C + 2: C + 2 + D]
	invoke = line[-1]

	solve(i, comb, opp, invoke)