from time import time
from math import sqrt

def nextCase():
	fileName = "C-small-attempt1.in"
	n = None
	for line in open(fileName, 'r').readlines():
		if None == n: n = int(line)
		else:
			yield tuple([int(x) for x in line.split(' ')])



def solve(T):
	def isPalindrome(x):
		x = str(x)
		for i in range(len(x)//2):
			if x[i] != x[len(x) - 1 - i]: return False

		return True

	def lowBound(x):
		y = int(sqrt(x))
		if y**2 == x: return y
		else: return y + 1

	def highBound(x):
		return int(sqrt(x))

	A, B = T
	low, high = lowBound(A), highBound(B)

#	print(low, high)
	return sum([1 for x in range(low, high + 1) if isPalindrome(x) and isPalindrome(x**2)])

start = time()

i = 1
for T in nextCase():
	print("Case #%d: %s" % (i, solve(T)))
	i += 1


#print(time() - start)
