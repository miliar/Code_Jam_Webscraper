import sys

def makeFarm(C, F, cookies, totalFarmTime):
	return totalFarmTime + C / cookies, cookies + F


fin  = open("B-large.in", "r")
fout = open("output_1s.txt", "w")

case = int(fin.readline().strip())
for c in xrange(case):
	[C, F, X] = map(float, fin.readline().strip().split())
	minTime = X / 2.0
	totalFarmTime = 0.0
	cookies = 2.0
	totalFarmTime, cookies = makeFarm(C, F, cookies, totalFarmTime)
	while minTime > totalFarmTime + X / cookies:
		minTime = totalFarmTime + X / cookies
		totalFarmTime, cookies = makeFarm(C, F, cookies, totalFarmTime)
	fout.write("Case #" + str(c + 1) + ": " + str(minTime) + "\n")

fin.close()
fout.close()