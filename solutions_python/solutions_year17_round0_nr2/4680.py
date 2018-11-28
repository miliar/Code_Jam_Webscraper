import cjio


def getDigitsReversed(num):
	n = num
	digs = []
	while True:
		digs.append(int(n%10))
		n = int(n/10)
		if n == 0:
			break
	return digs
print(getDigitsReversed(123))
assert(getDigitsReversed(123) == [3,2,1])
assert(getDigitsReversed(0) == [0])
print(getDigitsReversed(11111))
assert(getDigitsReversed(111111) == [1,1,1,1,1,1])

def isNonAscending(aList):
	for i in range(len(aList) - 1):
		if aList[i] < aList[i+1]:
			return False
	return True
assert(isNonAscending([1,2,3]) == False)

def isTidy(num):
	digits = getDigitsReversed(num)
	return isNonAscending(digits)
assert(isTidy(132)==False)
assert(isTidy(1)==True)
assert(isTidy(111)==True)
assert(isTidy(123)==True)
assert(isTidy(321)==False)

def tidyProblem(n):
	# returns largest non-tidy integer in [1,n]
	i = n
	while not  isTidy(i):
		i -= 1
	return i
print(tidyProblem(132))
assert(tidyProblem(132) == 129)
assert(tidyProblem(1000) == 999)
assert(tidyProblem(7) == 7)
# assert(tidyProblem(111111111111111110) == 99999999999999999)



if __name__ == '__main__':
	inputFile = r"C:\Users\ed\codejam2017\B-small-attempt0.in"
	outputFile = r"C:\Users\ed\codejam2017\B-small-attempt0.out"

	n, data = cjio.parseFile(inputFile)
	res = []
	for i in data:
		res.append(tidyProblem(int(i)))

	cjio.generateOutput(outputFile, res, n)
