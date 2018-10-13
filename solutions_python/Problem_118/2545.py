from math import sqrt

fp = open("C-small-attempt0.in", "r")
pf = open("out.txt", "w")


def isPalindrome(n):
	if n == n[::-1]:
		return True
	return False

def isSquare(n):
	s = sqrt(n)
	if s == int(s):
		return True
	return False

t = int(fp.readline())

for j in range(0, t):
	l = fp.readline()
	p = l.split(' ')

	c = 0
	
	for i in range(int(p[0]), int(p[1])+1):
		s = repr(i)
		if isPalindrome(s):
			if isSquare(i):
				q = repr(int(sqrt(i)))
				if isPalindrome(q):
					c += 1
	
	pf.write("Case #" + str(j+1) + ": " + str(c) + "\n")
