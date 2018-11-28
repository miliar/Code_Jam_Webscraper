import math


def solve(a, aCards, b, bCards):

	row1 = aCards[int(a) - 1]
	row2 = bCards[int(b) - 1]

	count = 0
	c = False
	for card in row1:
		if card in row2:
			c = card
			count += 1

	if count == 1:
		return c
	elif count > 1:
		return "Bad magician!"
	else:
		return "Volunteer cheated!"



name = "A-small-attempt0"
f = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(f.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	firstNumber = f.readline()
	firstCards = []
	for j in range(0, 4):
		firstCards.append(f.readline().strip().split(" "))
	secondNumber = f.readline()
	secondCards = []
	for k in range(0, 4):
		secondCards.append(f.readline().strip().split(" "))

	fout.write("Case #" + str(i + 1) + ": " + str(solve(firstNumber, firstCards, secondNumber, secondCards)) + "\n")
	#print "Case #" + str(i + 1) + ": " + str(solve(firstNumber, firstCards, secondNumber, secondCards)) + "\n"

f.close()
fout.close()