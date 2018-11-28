import math


def solve(a, b, k):

	count = 0
	i = 0
	while i < a:
		j = 0
		while j < b:
			if (i & j) < k:
				count += 1
			j += 1
		i += 1
	return count


name = "B-small-attempt0"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	a = int(line[0])
	b = int(line[1])
	k = int(line[2])

	fout.write("Case #" + str(i + 1) + ": " + str(solve(a, b, k)) + "\n")
	#print "Case #" + str(i + 1) + ": " + str(solve(a, b, k))

fi.close()
fout.close()