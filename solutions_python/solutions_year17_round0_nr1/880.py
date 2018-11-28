import math
import random


def solve(pancakes, numFlip):
	num = len(pancakes)
	numPos = pancakes.count("+")
	numNeg = num - numPos

	if (numNeg == 0):
		return 0

	if (numNeg % 2 == 1 and numFlip % 2 == 0):
		return "IMPOSSIBLE"

	counter = 0
	pancakes = list(pancakes)
	i = 0
	while pancakes.count("-") and i <= num - numFlip:
		if pancakes[i] == "-":
			counter += 1
			for j in range(i, i+numFlip):
				if pancakes[j] == "+":
					pancakes[j] = "-"
				else:
					pancakes[j] = "+"
		i += 1

	if pancakes.count("-"):
		return "IMPOSSIBLE"
	else:
		return counter


name = "A-large"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	#line = map(int, line)

	result = str(solve(line[0], int(line[1])))
	fout.write("Case #" + str(i + 1) + ": " + result + "\n")
	print "Case #" + str(i + 1) + ": " + result

fi.close()
fout.close()