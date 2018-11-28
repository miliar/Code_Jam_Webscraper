import psyco
import math
import sys

INPUT_FILENAME = "A-large"

sample = file("%s.in" % INPUT_FILENAME, "rb")
output = file("%s.out" % INPUT_FILENAME, "wb")

psyco.full()

def toOutput(line):
	print line
	output.write("%s\n" % line)

def solve(caseNumber, N, table):
	wins = [0] * N
	loses = [0] * N

	WP = [0] * N
	OWP = [0] * N
	OOWP = [0] * N

	for i in xrange(N):
		wins[i] = table[i].count('1')
		loses[i] = table[i].count('0')

		WP[i] = float(wins[i]) / (wins[i] + loses[i])
	
	for i in xrange(N):
		OWPcount = 0
		OWPavg = 0

		for j in xrange(N):
			if i == j:
				continue

			winsOWP = wins[j]
			losesOWP = loses[j]

			if table[j][i] == '1':
				winsOWP -= 1
			elif table[j][i] == '0':
				losesOWP -= 1
			else:
				continue
			
#			print i, j, winsOWP, losesOWP
			OWPavg += float(winsOWP) / (winsOWP + losesOWP)
			OWPcount += 1
	
		if OWPcount:
			OWP[i] = (OWPavg / float(OWPcount))

	for i in xrange(N):
		OOWPcount = 0

		for j in xrange(N):
			if table[i][j] != '.':
				OOWPcount += 1
				OOWP[i] += OWP[j]
		
		OOWP[i] = float(OOWP[i]) / OOWPcount

	toOutput("Case #%d:" % caseNumber)

	for i in xrange(N):
		toOutput("%.12f" % (0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]))

numberOfTestCases = int(sample.readline())
for i in xrange(1, numberOfTestCases + 1):
	N = int(sample.readline())

	table = [0] * N
	for j in xrange(N):
		table[j] = [0] * N

	for j in xrange(N):
		line = sample.readline().strip()
		for k in xrange(N):
			table[j][k] = line[k]

	solve(i, N, table)