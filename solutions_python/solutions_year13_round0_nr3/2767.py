import math
inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")

numberOfTestCases = int(inputFile.readline())

def main():
	for i in range(numberOfTestCases):
		lower, upper = [int(num) for num in inputFile.readline().strip().split()]
		count = 0
		for j in range(lower,upper+1):
			if (isPalindrome(j) and isPerfectSquare(j) and isPalindrome(int(math.sqrt(j)))):
				count = count + 1

		outputFile.write("Case #" + str(i+1) + ": " + str(count) + "\n")

def isPalindrome(num):
	num = str(num)
	for i in range(0, int(len(num)/2)):
		if (num[i] != num[len(num)-1-i]):
			return False
	return True

def isPerfectSquare(num):
	if int(math.sqrt(num))**2 != num:
		return False
	return True

main()