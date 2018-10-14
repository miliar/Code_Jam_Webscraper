import math
import sys

# Return true if input string is a palindrome	
def isPalindrome(s):
	if len(s) == 1:
		return True
	else:
		half = len(s) // 2
		firstHalf = s[:half]
		secondHalf = s[-half:]
		secondHalf = secondHalf[::-1]
		if firstHalf == secondHalf:
			return True
		else:
			return False
		
# Return true if input integer is a perfect square
def isSquare(i):
	root = math.sqrt(i)
	if root == int(root):
		return True
	else:
		return False
	


# Read data file into a list
lines = []
with open(sys.argv[1], "r", encoding="utf-8") as data_file:
	for line in data_file:
		lines.append(line.rstrip('\n'))


# Get total number of test cases
test_cases = int(lines[0])
del lines[0]

# Process each test case
case = 0
for line in lines:
	case += 1
	count = 0
	min = int(line.split(" ")[0])
	max = int(line.split(" ")[1])
	for i in range(min, (max + 1)):
		if isPalindrome(str(i)):
			if isSquare(i):
				root = int(math.sqrt(i))
				if isPalindrome(str(root)):
					count += 1
	
	print("Case #" + str(case) + ": " + str(count))