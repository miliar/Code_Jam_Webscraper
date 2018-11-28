import math

def isPalindrome(num):
	s =  str(num)
	if s == s[::-1]: return True
	else: return False


max_ = 10**14 + 10
savedOnes = []

upper = int(math.floor(math.sqrt(max_)))
for i in range(1,upper+1):
	if isPalindrome(i) and isPalindrome(i**2): savedOnes.append(i)



T = input()

for t in range(T):
	a,b = map(int,raw_input().strip().split())

	"""
	upper = int(math.floor(math.sqrt(b)))
	lower = int(math.ceil(math.sqrt(a)))
	count = 0

	for i in range(lower,upper+1): 
		if isPalindrome(i) and isPalindrome(i**2): count += 1
	"""

	count = 0
	for elem in savedOnes:
		if elem**2 > b: break
		if elem**2 <= b and elem**2>=a: count += 1


	print "Case #%d: %d" % (t+1, count)

