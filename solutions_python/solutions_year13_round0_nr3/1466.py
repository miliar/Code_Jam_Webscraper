import sys
import math

def isPalindrome(number):
				numDigits = int(math.floor(math.log(number,10)))+1
				for i in range(numDigits/2):
								lastDig = number/(10**(i)) % 10
								firstDig = number/(10**(numDigits-i-1)) % 10
								if lastDig != firstDig:
												return False
				return True


def numFairAndSquare(minNum, maxNum):
				sqrtmin = int(math.ceil(math.sqrt(minNum)))
				sqrtmax = int(math.floor(math.sqrt(maxNum)))
				ret = 0
				for i in range(sqrtmin, sqrtmax+1):
								if isPalindrome(i) and isPalindrome(i*i):
												ret += 1
				return ret


if __name__ == '__main__':
				if len(sys.argv) < 2:
								print 'need file'
								sys.exit(1)

				lines = [x.strip() for x in open(sys.argv[1]).readlines()]
				numCases = int(lines[0])
				lines = lines[1:]

				currIdx = 0
				for caseNum in range(numCases):
								(minNum, maxNum) = map(int, lines[caseNum].split())

								result = numFairAndSquare(minNum, maxNum)
								print "Case #%d: %d" % ((caseNum+1), result)

								caseNum += 1
