import sys

# def bitWiseAnd(str1, str2):
# 	diff = len(str1) - len(str2)
# 	if diff > 0:
# 		str1
def howManyWays(A, B, K):
	ways = 0
	for i in range(0, A):
		for j in range(0, B):
			bit = i&j
			if bit < K and bit > -1:
				ways += 1
	return ways

infile = sys.argv[1]
outfile = sys.argv[2]

inf = open(infile)
outf = open(outfile, 'w')
numTestCases = int(inf.readline())

for testcase in range(1, numTestCases+1):
	read = inf.readline().split()
	A = int(read[0])
	B = int(read[1])
	K = int(read[2])
	outf.write('Case #'+str(testcase)+': '+str(howManyWays(A, B, K))+'\n')