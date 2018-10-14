import math
import itertools


def solve(n, cars):

	j = 0
	while j < len(cars):
		cars[j] = simplify(cars[j])
		j += 1

	count = 0
	for e in list(itertools.permutations(cars, len(cars))):
		if valid(e):
			count += 1

	return count

def valid(cars):

	h = []
	seq = "".join(cars)
	prevChar = ""

	for char in seq:
		included = char in h
		if prevChar:
			if char != prevChar and included:
				return False
		if not included:
			h.append(char)
		prevChar = char
	return True

def simplify(car):

	l = list(car)
	i = 1
	while i < len(l):
		if l[i] == l[i-1]:
			del l[i]
		else:
			i += 1

	return "".join(l)


name = "B-small-attempt1"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	n = int(fi.readline().strip())
	cars = fi.readline().strip().split(" ")

	fout.write("Case #" + str(i + 1) + ": " + str(solve(n, cars)) + "\n")
	#print "Case #" + str(i + 1) + ": " + str(solve(n, cars))

fi.close()
fout.close()