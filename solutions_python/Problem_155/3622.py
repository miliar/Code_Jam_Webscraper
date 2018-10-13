INPUT_FILE = 'A-small-attempt0.in'
OUTPUT_FILE = 'A-small.out'
answer = ''

def getCountOfAdditionalPeople(rawString):
	stayingPeople = 0
	additionalPeople = 0
	for i, c in enumerate(rawString[2:int(rawString[:1]) + 3]):
		if (stayingPeople < i and int(c) > 0):
			additionalPeople += i - stayingPeople
			stayingPeople = i
		stayingPeople += int(c)
	return additionalPeople

with open(INPUT_FILE) as inFile:
	content = inFile.readlines()

for caseNum in range(1, int(content[0]) + 1):
	answer += 'Case #' + str(caseNum) + ': ' + str(getCountOfAdditionalPeople(content[caseNum][:-1])) + "\n"

with open(OUTPUT_FILE, 'w') as outFile:
	outFile.write(answer)

# print getCountOfAdditionalPeople('4 11111')
# print getCountOfAdditionalPeople('1 09')
# print getCountOfAdditionalPeople('5 110011')
# print getCountOfAdditionalPeople('0 1')