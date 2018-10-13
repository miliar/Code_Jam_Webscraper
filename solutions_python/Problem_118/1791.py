import math

INPUT_SAMPLE = 'C-sample.in.txt'
INPUT_SMALL  = 'C-small-attempt1.in.txt'
INPUT_LARGE_ONE  = 'C-large.in.txt'
INPUT_LARGE_TWO  = 'C-large.in.txt'

INPUT = INPUT_SMALL


# a number is fair and square if both the number and its square root are integer palindromes

# construct a sieve of such numbers
# start from 1 until sqrt(max(B)) , for large_two, max(b) = 10^14
# and if both the number, and it's square are palindromes, then store the square

def isStringPalindrome(aString):

	if len(aString) == 1:
		return True

	if (aString[0] == aString[-1]):
		# something like 11, 22
		if len(aString) == 2:
			return True
		# keep going
		else :
			return isStringPalindrome(aString[1:-1])

	return False

# returns a list of fair and squares values up to maxNo
def constructListOfFairSquaresUpTo(aMaxNo):
	result = []

	# stop at the square root of maxNo
	global stopPoint
	global currPoint
	stopPoint  = math.sqrt(aMaxNo)
	stopPoint  = int(math.floor(aMaxNo))
	stopPoint += 1

	currPoint = 0

	while True:

		currPoint += 1

		if currPoint >= stopPoint:
			break

		if (isStringPalindrome(str(currPoint))):

			numberSquared = currPoint * currPoint

			if (isStringPalindrome(str(numberSquared))):
				result.append(numberSquared)

	return result


# up to 1001
listOfFairAndSquares = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001]

f = open("output.txt", 'w')

lines = open(INPUT, 'r').readlines()
lines = [x.rstrip('\n') for x in lines]

noTestCases = int(lines[0])
lines = lines[1:]

for currTestCase in xrange(0, noTestCases):
	if (currTestCase !=0):
		f.write("\n")

	f.write('Case #' + str(currTestCase+1) + ": ")

	A = int(lines[0].split(' ')[0])
	B = int(lines[0].split(' ')[1])

	startIdx = 0
	endIdx = len(listOfFairAndSquares) -1

	for currNo in listOfFairAndSquares:
		if currNo >= A:
			startIdx = listOfFairAndSquares.index(currNo)
			break

	for currNo in listOfFairAndSquares[startIdx:]:
		if currNo > B:
			endIdx = listOfFairAndSquares.index(currNo)
			break

	noOfResults = endIdx - startIdx

	f.write(str(noOfResults))

	# trim the lines for the next test case
	lines = lines[1:]



