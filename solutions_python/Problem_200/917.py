import math
import random


def solve(n):
	n = list(n)
	n = map(int, n)
	changed = True
	while changed:
		changed = False
		for i in range(0, len(n)-1):
			if n[i] > n[i+1]:
				changed = True
				n[i] -= 1
				for j in range(i+1, len(n)):
					n[j] = 9

	n = map(str, n)
	return int("".join(n))


name = "B-large"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	# line = map(int, line)

	result = str(solve(line[0]))
	fout.write("Case #" + str(i + 1) + ": " + result + "\n")
	print "Case #" + str(i + 1) + ": " + result

fi.close()
fout.close()