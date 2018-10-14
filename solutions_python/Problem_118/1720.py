import math

def isPalindrome(s):
	if s == s[::-1]:
		return 1
	else:
		return 0

f = open ("b.in", 'r')

g = open ("b.txt", 'w')

T = int(f.readline())

i = 0

for line in f:
	i = i + 1

	result = 0
	
	[A, B] = [int(x) for x in line.split()]

	for n in range(A, B + 1):
		m = math.sqrt(n)
		p = int(m)
		if p * p == n:
			if isPalindrome(str(p)) and isPalindrome(str(n)):
				result = result + 1

	g.write ("Case #" + str(i) + ": " + str(result) + "\n")
