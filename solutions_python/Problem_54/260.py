def gcd(a, b):
	while True:
		if a >= b:
			a = a % b
			if a == 0:
				return b
		else:
			b = b % a
			if b == 0:
				return a

def gcdList(numbers):
	cnt = len(numbers)

	if cnt == 0:
		return 1
	elif cnt == 1:
		return numbers[0]
	else:
		res = gcd(numbers[0], numbers[1])
		for i in range(2, cnt):
			res = gcd(res, numbers[i])
		return res

def getMinimumSeconds(numbers):
	numbers.sort()
	diffs = []
	for i in range(len(numbers)-1):
		d = numbers[i+1] - numbers[i]
		if d != 0:
			diffs.append(d)

	g = gcdList(diffs)
	m = numbers[0] % g
	if m == 0:
		return 0
	else:
		return g - m

import sys
#import pdb

fileNamePrefix = sys.argv[1]
fileNameIn = fileNamePrefix + ".in"
fileNameOut = fileNamePrefix + ".out"

fileIn = open(fileNameIn, 'r')
lines = fileIn.readlines()

testcnt = int(lines[0])
idx = 1

fileOut = open(fileNameOut, 'w')

#pdb.set_trace()
for test in range(testcnt):
	line = lines[idx].split(' ')
	idx += 1

	numberCnt = int(line[0])
	numbers = []

	for numberStr in line[1:]:
		numbers.append(int(numberStr))

	res = getMinimumSeconds(numbers)
	fileOut.write("Case #{0}: {1}\n".format(test + 1, res))
