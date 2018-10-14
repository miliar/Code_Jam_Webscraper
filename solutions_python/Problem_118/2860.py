import sys
import math

N = int(sys.stdin.readline())
total = 0


def isPalindrome(number):
	
	if len(str(number)) == 1:
		return True

	res = False
	digits = list(str(number))
	endOfDigits = int(math.floor(len(str(number))))-1

	loopRange = int(math.floor(len(str(number))/2))

	for i in range(loopRange):
		res = (digits[i] == digits[endOfDigits-i])

	return res


def searchFirstPalindrome(low,up):
	base = low
	while not isPalindrome(base) and low < up:
		base += 1

	return base

def is_square(apositiveint):
	if apositiveint == 0 or apositiveint == 1:
		return True
	x = apositiveint // 2
	seen = set([x])
	while x * x != apositiveint:
		x = (x + (apositiveint // x)) // 2
		if x in seen: return False
		seen.add(x)
	return isPalindrome(x)

def addPalindrome(depth,length,number,up,first):
	base = number
	for i in range(10):
		if number <= up and len(str(number)) <= length:
			if is_square(number) and first:
				global total
				total += 1
			else:
				first = True
			if depth+1 < math.ceil(length/float(2)):
				addPalindrome(depth+1,length,number,up,False)
		else:
			return 10**length+1

		firstDigit = list(str(number))[0]

		if length%2 != 0 and depth+1 > length/2:
			number = base + (i+1)*(10**depth)
		else:
			number = base + (i+1)*(10**(length-1-depth)) + (i+1)*(10**depth)

		newfirstDigit = list(str(number))[0]

		if newfirstDigit != firstDigit and len(str(number)) == length:
			number = int(newfirstDigit)*(10**(length-1))+int(newfirstDigit)
			i=0



	return 10**length+1



for i in range(N):
	low, up = (int(w) for w in sys.stdin.readline().split())
	total = 0

	number = searchFirstPalindrome(low,up)

	while len(str(number)) < 2 and number <= up:
		if is_square(number):
			total += 1
		number += 1


	currentLength = len(str(number))
	while number <= up:
		number = addPalindrome(0,len(str(number)),number,up,True)
		currentLength = len(str(number))

	sys.stdout.write('Case #'+str(i+1)+': '+str(total)+'\n')