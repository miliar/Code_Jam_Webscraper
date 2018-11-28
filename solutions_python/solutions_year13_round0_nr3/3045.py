def isPalindrome(i):
	stringI = str(i)
	lengthI = len(stringI)
	for i in range(0,lengthI / 2 + 1):
		if stringI[i] != stringI[lengthI - i - 1]:
			return False
	return True

def numberOfNiceSquares(a,b):
	squares = 0
	for i in range(a,b + 1):
		squared = float(i)**.5
		if isPalindrome(i) and squared % 1 == 0 and isPalindrome(int(squared)):
			squares += 1
	return squares

numOfCases = int(raw_input())
testCases = []
for i in range(numOfCases):
	case = str(raw_input())
	if not " " in case:
		case = [0,int(case)]
	else:
		case = case.split(" ")
		case[0] = int(case[0])
		case[1] = int(case[1])
	testCases.append(case)

for caseNum in range(1,numOfCases + 1):
	print "Case #" + str(caseNum) + ": " + str(numberOfNiceSquares(testCases[caseNum - 1][0], testCases[caseNum - 1][1]))