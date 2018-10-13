import math
import random


def solve(stalls, users):

	if stalls == users:
		return map(str,[0,0])

	while users > 1:
		users -= 1
		newStalls1 = int(math.floor((stalls - 1) / 2.0))
		newStalls2 = int(math.ceil((stalls - 1) / 2.0))

		newUsers1 = int(math.floor(users / 2.0))
		newUsers2 = int(math.ceil(users / 2.0))

		if users % 2 == 1:
			stalls = newStalls2
			users = newUsers2
		else:
			stalls = newStalls1
			users = newUsers1

	newStalls1 = int(math.floor((stalls - 1) / 2.0))
	newStalls2 = int(math.ceil((stalls - 1) / 2.0))
	return map(str, [newStalls2, newStalls1])


name = "C-small-2-attempt0"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	line = map(int, line)

	result = " ".join((solve(line[0], line[1])))
	fout.write("Case #" + str(i + 1) + ": " + result + "\n")
	print "Case #" + str(i + 1) + ": " + result

fi.close()
fout.close()