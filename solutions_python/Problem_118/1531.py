import string
import math

#Problem C: Fair and Square
def isPalindrome(_num):
	reverse = 0
	num = _num
	while num > 0:
		digit = num % 10
		reverse = reverse*10 + digit
		num = int(num/10)
	if reverse == _num:
		return True	
	return False

def isSquareofPalindrome(num):
#	if not isSquare(num):
#		return False
	root = math.sqrt(num)
	if not isPalindrome(root):
		return False
	return isPalindrome(num)	

def isSquare(num):
	root = math.floor(math.sqrt(num))
	if root**2 == num:
		return True
	return False	

#Initialize up to MAX
MAX = 10**14
squareList = [] 
sPList = []
#Build the lists up to the MAX before input
for i in range(1,int(math.floor(math.sqrt(MAX)))):
	num = i**2
	squareList.append(num)
	if isSquareofPalindrome(num) and isPalindrome(num):
		sPList.append(num)

#Main implementation
inFile = open("input.txt", 'r')
outFile = open("output.txt", 'w')

T = int(inFile.readline())

for i in range(T):
	line = inFile.readline().partition(' ')
	A = int(line[0])
	B = int(line[2])
	count = 0
	for x in sPList:
		if x >= A and x <= B:
			if isSquareofPalindrome(x) and isPalindrome(x):
				count += 1
	outFile.write("Case #" + str(i+1) + ": " + str(count) + '\n')
for x in sPList:
	print x 
