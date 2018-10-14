from math import sqrt

def checkPalindrome(number):
	number = str(number)
	newNumber = ""
	for a in range(len(number)-1,-1,-1):
		newNumber += number[a]
	if number == newNumber:
		return True
	else:
		return False

def checkRoot(number):
	if sqrt(number) % 1 == 0:
		return True
	else:
		return False

i = open("C-small-attempt0.in", "r")
o = open("C-small-attempt0-output.txt", "w")

T = int(i.readline())
print "Test Cases (T):", T

for t in range(T):
	counter = 0 #counts number of 'fair and square' values
	AandB = i.readline().split()
	A = int(AandB[0])
	B = int(AandB[1])

	for x in range(A,B+1):
		if checkPalindrome(x):
			if checkRoot(x):
				if checkPalindrome(int(sqrt(x))):
					counter += 1
	print "Case #" + str(t+1) + ": " + str(counter)
	o.write("Case #" + str(t+1) + ": " + str(counter) + "\n")