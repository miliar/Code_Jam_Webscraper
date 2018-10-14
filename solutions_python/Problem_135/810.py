import sys

def getCandidate(f):
	matrix = list()
	row = int(fin.readline().strip()) - 1
	for i in range(4):
		matrix.append(map(int, fin.readline().strip().split()))
	return matrix[row]

def getIntersection(c1, c2):
	intersection = list()
	for num in c1:
		if num in c2:
			intersection.append(num)

	return intersection


fin  = open("A-small-attempt1.in", "r")
fout = open("output_1s.txt", "w")

case = int(fin.readline().strip())
for c in xrange(case):
	candidate1 = getCandidate(fin)
	candidate2 = getCandidate(fin)
	answer = getIntersection(candidate1, candidate2)
	if len(answer) == 0:
		fout.write("Case #" + str(c + 1) + ": Volunteer cheated!\n")
	elif len(answer) == 1:
		fout.write("Case #" + str(c + 1) + ": " + str(answer[0]) + "\n")
	else:
		fout.write("Case #" + str(c + 1) + ": Bad magician!\n")

fin.close()
fout.close()