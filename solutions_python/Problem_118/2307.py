import math


def solve(start, end):
	count = 0
	for i in range(start, end + 1):
		if isPalindrome(i):
			numberRoot = math.sqrt(i)
			if isWhole(numberRoot):
				numberRoot = int(numberRoot)
				if isPalindrome(numberRoot):
					count = count + 1
	return count

def isPalindrome(number):
	numberAsString = str(number)
	if numberAsString == numberAsString[::-1]:
		return True
	else:
		return False

def isWhole(number):
	if number % 1 == 0:
		return True
	else:
		return False

def main():
	inFile = open("C-small-attempt0.in", "r")
	outFile = open("problem.out", "w")
	
	lines = inFile.read().split()
	inFile.close()
	    
	numberOfCases = int(lines[0])
	lines.pop(0)
	
	for i in range(numberOfCases):
		start = int(lines[0])
		lines.pop(0)
		end = int(lines[0])
		lines.pop(0)
		result = solve(start, end)
		result = "Case #" + str(i + 1) + ": " + str(result) + "\n"
		print(result)
		outFile.write(result);
	outFile.close()
   
main()