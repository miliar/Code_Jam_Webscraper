import psyco
import math
import sys

INPUT_FILENAME = "B-small-attempt2"

sample = file("%s.in" % INPUT_FILENAME, "rb")
output = file("%s.out" % INPUT_FILENAME, "wb")

psyco.full()

def toOutput(line):
	print line
	output.write("%s\n" % line)

def solve(caseNumber, L, t, N, C, A):
	stations = (A * ((N // C) + 1))[:N]

	pos = -1
	value = 0

	if L == 0:
		toOutput("Case #%d: %d" % (caseNumber, sum(stations) * 2))
		return

	if stations[0] > t:
		value = stations[0] - (t / 2.0)
		pos = 0
	else:	
		stations2 = [x * 2 for x in stations]
		for i in xrange(1, len(stations2)):
			stations2[i] += stations2[i - 1]

			if stations2[i] > t:
				value = stations[i] - ((t - stations2[i - 1]) / 2.0)
				pos = i
				break
		
		if pos == -1:
			toOutput("Case #%d: %d" % (caseNumber, sum(stations) * 2))
			return
	
	sortedStations = sorted(stations[pos + 1:], reverse = True)[:L]

	cost = sum(stations) * 2

	if not sortedStations:
		# print L, t, N, C, A
		cost -= value
	else:
		if sortedStations[-1] < value:
			sortedStations[-1] = value
		
		cost -= sum(sortedStations)

	toOutput("Case #%d: %d" % (caseNumber, cost))

numberOfTestCases = int(sample.readline())
for i in xrange(1, numberOfTestCases + 1):
	values = map(int, sample.readline().split())

	L, t, N, C = values[:4]
	A = values[4:]

	solve(i, L, t, N, C, A)