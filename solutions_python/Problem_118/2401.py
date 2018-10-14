
# python3.3

import math

INPUT_FILE = "C-small-attempt0.in"
OUTPUT_FILE = "fair_output.txt"


def isSquareAndFair(number):
	# print(int(math.sqrt(number)), math.sqrt(number), math.sqrt(number).is_integer())
	return isPalindrom(number) and isPalindrom(int(math.sqrt(number))) and math.sqrt(number).is_integer()
		   # and int(math.sqrt(number)) == math.sqrt(number)

def isPalindrom(number):
	string = str(number)
	for i in range(len(string)):
		if string[i] != string[len(string)-i-1]:
			return False
	return True


# read file
nCases = 0
parsedList = []
info = []
newCase = True
first = True
previousLen = 0

with open(INPUT_FILE, "r") as fd:
	for line in fd:	

		if nCases == 0:
			nCases = int(line)
			continue
		parsedList.append(list(int(x.rstrip('\n')) for x in line.split(' ')))

# print(nCases)
# print(parsedList)

fd = open(OUTPUT_FILE, "w")

for i in range(nCases):
	firstN = parsedList[i][0]
	secondN = parsedList[i][1]

	count = 0
	for j in range(firstN,secondN+1):
		if isSquareAndFair(j):
			count += 1

	string = "Case #" + str(i+1) + ": " + str(count)
	if i < nCases - 1:
		string += "\n"
	fd.write(string)

fd.close()

# print(isSquareAndFair(676))

