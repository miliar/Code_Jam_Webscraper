def formatLine(line):
	s = line.split()
	s = [int(i) for i in s]

	return s

def solveTestCase(line):
	line = formatLine(line)
	omino = line[0]
	m = line[1]
	n = line[2]

	if (m*n) % omino != 0:
		return "RICHARD"
	if omino == 4 and min(m,n) <= 2:
		return "RICHARD"
	if omino == 3 and min(m,n) == 1:
		return "RICHARD"

	return "GABRIEL"



data = open("testfile.txt", 'r')
out = open("answer.txt", "w")
numberCases = int(data.readline())

for i in range(numberCases):
	s = "Case #{0:d}: {1:s}\n".format(i+1, solveTestCase(data.readline()))
	print s
	out.write(s)


		