import math

def isPalindrome(n):
	s = str(n)
	return s == s[::-1]

# Yields palindromes with the specified number of digits
def palindromeOfLength(b):
	if b == 1:
		for i in range(1, 10):
			yield i
	elif b == 2:
		for i in range(1, 10):
			yield 11 * i
	else:
		for i in range(1, 10):
			for p in palindromeOfLength(b - 2):
				yield i * (10 ** (b - 1) + 1) + 10 * p

# Yields palindromes >= n
def palindrome(n):
	b = len(str(int(math.floor(n))))
	ff = True
	while True:
		for i in palindromeOfLength(b):
			if ff:
				if i < n:
					continue
				ff = False
			yield i
		b += 1
	
			
# Read file
with open('in3.txt', 'r') as f:
	count = int(f.readline())
	for i in xrange(count):
		begin, end = map(int, f.readline().strip().split(' '))
		
		# Count the number of palindromes
		c = 0
		for p in palindrome(math.sqrt(begin)):
			p2 = p * p
			if p2 > end:
				break
			
			if isPalindrome(p2):
				c += 1
				
		print "Case #" + str(i + 1) + ": " + str(c)