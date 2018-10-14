import math

def solve(A, B):
	count = 0
	a = int(math.ceil(math.sqrt(A)))
	b = int(math.floor(math.sqrt(B)))
	for x in range(a, b+1):
		if is_palindrome(x) and is_palindrome(x*x):
			count = count + 1
	return count

def is_palindrome(x):
	return str(x) == str(x)[::-1]

File = open("C-small-attempt0.in", "r")
f = []
for line in File:
	f.append(line.split())
for i in range(int(f[0][0])):
	A = int(f[i+1][0])
	B = int(f[i+1][1])
	print "Case #%d:" %(i+1), solve(A, B)