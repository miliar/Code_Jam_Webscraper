import sys
import math

def main(filename):
	result = ''
	file = open(filename)
	numberOfTests = int(file.readline())
	for i in range(numberOfTests):
		ab = [int(num) for num in file.readline().split()]
		a = ab[0]
		b = ab[1]
		result += 'Case #%d: %s\n' % (i+1,solvePalindromes(a,b))
	file.close()
	return result
	
def solvePalindromes(a,b):
	result = 0
	lowerA = int(math.ceil(math.sqrt(a)))
	lowerB = int(math.floor(math.sqrt(b)))
	for num in range(lowerA, lowerB+1):
		if isPalindrome(num) and isPalindrome(num*num):
			result += 1
	return result
	
def isPalindrome(a):
	stringA = str(a)
	for index in range(len(stringA)/2):
		if stringA[index] != stringA[len(stringA)-1-index]:
			return False
	return True
			
if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'Not enough files specified'
		sys.exit(1)
	inputfilename = sys.argv[1]
	outputfilename = sys.argv[2]
	result = main(inputfilename)
	outputfile = open(outputfilename, 'w')
	outputfile.write(result)
	outputfile.close()
	print result