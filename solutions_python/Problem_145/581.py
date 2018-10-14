import math


def solve(a, b):
	generations = 40
	gen = 1

	if a == 1 and b == 1:
		return 0

	if (math.log(b, 2) % 1) != 0:
		return "impossible"

	while a < b/2 and gen <= 40:
		gen += 1
		b /= 2

		#print a, b

		if b % 2 == 1:
			return "impossible"

	if gen > 40:
		return "impossible"
	else:
		return gen


name = "A-small-attempt2"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split("/")
	a = int(line[0])
	b = int(line[1])

	fout.write("Case #" + str(i + 1) + ": " + str(solve(a, b)) + "\n")
	#print "Case #" + str(i + 1) + ": " + str(solve(a, b))

fi.close()
fout.close()