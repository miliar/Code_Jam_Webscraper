import sys;
import math;
import pprint;

def generatePalindromes(start, end):
	startingSeedLength = len(str(start))//2
	
	if(startingSeedLength < 2):
		startingSeed = 1;
	else:
		startingSeed = int(math.pow(10, startingSeedLength-1))
	endStringLength = (len(str(end))//2)+1
	palindromes = [];
	if(start < 10):
		if(end >= 10):
			palindromes.extend(range(start, 10))
		else:
			palindromes.extend(range(start, end+1))
	
	for i in range(startingSeed, int('9' * endStringLength)):
		begining = str(i)
		reverse = str(i)[::-1]
		middles = ["", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
		for mid in middles:
			palindrome = int(begining + mid + reverse)
			if(palindrome <= end):
				if(palindrome >= start):
					palindromes.append(palindrome)
			else:
				if(mid == ""):
					return palindromes
				else:
					break
	return palindromes
	
def solve(palindromes):
	result = []
	for pal in palindromes:
		sqr = math.sqrt(pal)
		if(((sqr % 1) == 0)):
			reversed = list(str(int(sqr)))
			reversed.reverse()
			if(str(int(sqr)) == ''.join(reversed)):
				result.append(pal)
	return len(result)

numberOfCases = int(sys.stdin.readline())
for caseNumber in range(1, numberOfCases + 1):
	numberRange = [int(i) for i in sys.stdin.readline().split()]
	result= solve(generatePalindromes(numberRange[0], numberRange[1]))
	sys.stdout.write("Case #" + str(caseNumber) + ": " + str(result))
	if(caseNumber != numberOfCases):
		sys.stdout.write("\n")
		