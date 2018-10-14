import sys


if len(sys.argv) != 2:
	sys.exit("Please specify test input file")
inputFilePath = sys.argv[1]
inputFile = open(inputFilePath, 'r')

numberOfTestCases = -1
testCases = []
lineNumber = 0
for line in inputFile.readlines():
	if 0 == lineNumber:
		numberOfTestCases = long(line)
	else:
		tmp = line.rstrip('\n').split(' ');
		start = long(tmp[0])
		end = long(tmp[1])
		testCases.append([start, end])
	lineNumber += 1

inputFile.close()

######################################

def isPalindrome(str):
    x = 0
    # len/2 is num of iter needed for guarantee
    while x < (len(str)/2):
        # on pass n, compare nth letter and nth to last letter
        if str[x+0] is str[-(1+x)]:
            # then increment the n counter
            x += 1
        else:
            return False
    return True

#palindromes = [-1] * pow(10, 100)

def calculate(start, end):
	i = start
	n = 0
	while i <= end:
		if isPalindrome(str(i)):
			s = pow(i, 0.5)
			if 0 == s % 1 and isPalindrome(str(long(s))):
				n += 1
		i += 1
	return n

#####################################

# palindromes = [-1] * 1000
#GOOGOL = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# i = 1

#print GOOGOL - 1000
#print pow(GOOGOL, 0.5)

for i in range(0 , len(testCases)):
	print "Case #" + str(i + 1) + ": " + str(calculate(testCases[i][0], testCases[i][1]))
