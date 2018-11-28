import math

def isPalindrome(n):
	my_str = str(n)
	return my_str == my_str[::-1]



T = input()

for i in xrange(T):
	As,Bs = raw_input().split()
	A = int(As)
	B = int(Bs)
	numeror = int(math.ceil(A**(1/2.0)))
	while not isPalindrome(numeror):
		numeror += 1
	
	j = numeror**2

	counter = 0
	while j <= B:
		if isPalindrome(j):
			counter += 1
		numeror += 1
		while not isPalindrome(numeror):
			numeror += 1
		j = numeror**2
		

	print "Case #%d: %d" %(i+1,counter)