import math


def solve(rows, cols, width):

	if cols == width:
		return rows - 1 + width
	elif width == 1:
		return rows * cols
	else:
		return int(math.floor(cols / (1.0*width))) * (rows - 1) + width + int(math.ceil((cols - width) / (1.0*width)))



name = "A-large"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	line = map(int, line)

	fout.write("Case #" + str(i + 1) + ": " + str(solve(line[0], line[1], line[2])) + "\n")
	#print "Case #" + str(i + 1) + ": " + str(solve(line[0], line[1], line[2]))

fi.close()
fout.close()