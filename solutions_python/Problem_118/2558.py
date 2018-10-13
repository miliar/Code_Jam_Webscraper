import math

def isPalindrome(num):
	strNum = str(num)
	if strNum == strNum[::-1]:
		return True
	return False

def isSquare(num):
	if math.sqrt(num) - math.floor(math.sqrt(num)) == 0:
		return True
	return False

def main():
	checkBoard = []
	cntr = 1
	
	f = open("C-small-attempt0.in")
	count = int(f.readline())
	
	for line in f:
		fairSqrCounter = 0
		ranger = line.split()
		for i in range(int(ranger[0]),int(ranger[1])+1):
			if isPalindrome(i) and isSquare(i):
				if isPalindrome(int(math.sqrt(i))):
					fairSqrCounter += 1
		print("Case #"+str(cntr)+": "+str(fairSqrCounter))
		cntr += 1
			
		
	return 0

if __name__ == '__main__':
	main()
