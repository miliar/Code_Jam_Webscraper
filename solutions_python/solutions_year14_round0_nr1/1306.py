fi = open("input.txt")
fo = open("output.txt", "r+")

a = int(fi.readline())

for c in range(a):
	firstChoice = int(fi.readline())
	firstMatrix = []
	for i in range(4):
		firstMatrix.append(map(int, fi.readline().rstrip().split()))
	firstList = firstMatrix[firstChoice - 1]

	secondChoice = int(fi.readline())
	secondMatrix = []
	for i in range(4):
		secondMatrix.append(map(int, fi.readline().rstrip().split()))
	secondList = secondMatrix[secondChoice - 1]
	
	s = list(set(firstList).intersection(set(secondList)))

	if(len(s) == 0):
		fo.write("Case #" + str(c + 1) + ": Volunteer cheated!\n")
	elif(len(s) > 1):
		fo.write("Case #" + str(c + 1) + ": Bad magician!\n")
	else:
		fo.write("Case #" + str(c + 1) + ": " + str(s[0]) + "\n")