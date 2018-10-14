import math


def solve(strings, numStrings):

	#character order
	# string = [s[:] for s in strings[i]]

	ops = 0
	while len(strings[0]):
		counts = numStrings * [0]
		char = strings[0][0]
		count = 0
		for i in range(0, numStrings):
			string = strings[i]
			if (not len(string)) or string[0] != char:
				return "Fegla Won"
			else:
				while len(string) and string[0] == char:
					count += 1
					counts[i] += 1
					del string[0]
		#print "COUNT", count, counts
		med = round(count / numStrings)
		for c in counts:
			ops += abs(c - med)
	for g in strings:
		if len(g) > 0:
			return "Fegla Won"
	return int(ops)



name = "A-small-attempt1"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	numStrings = int(fi.readline().strip())
	strings = []
	for j in range(0, numStrings):
		strings.append(list(fi.readline().strip()))

	fout.write("Case #" + str(i + 1) + ": " + str(solve(strings, numStrings)) + "\n")
	#print "Case #" + str(i + 1) + ": " + str(solve(strings, numStrings))

fi.close()
fout.close()