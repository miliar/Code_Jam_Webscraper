import string

T = input()

def isPalindrome(word):
	for i in xrange(len(word)):
		if word[i] != word[len(word)-i-1]:
			return False
	return True
	
def isPerfectFairSquare(x):
	ans = 0
	if x >= 0:
		while ans*ans < x:
			ans = ans + 1

		if ans*ans != x:  # this if statement was nested inside the while
			return False
		else:
			return isPalindrome(str(ans)) and True
	return False

for t in xrange(T):
	A, B = raw_input().split()
	count = 0
	for i in xrange(int(A), int(B)+1):
		if isPalindrome(str(i)) and isPerfectFairSquare(i):
			count += 1
	print "Case #"+str(t+1)+": "+str(count)
