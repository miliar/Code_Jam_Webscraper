from math import *

def isPalyndrome(x):
	return str(x) == str(x)[::-1]

def countFair(A, B):
	start = int(ceil(sqrt(A)))
	end = int(floor(sqrt(B)))
	c = 0
	for i in range(start,end+1):
		if isPalyndrome(i):
			n = i * i
			if isPalyndrome(n):
				c += 1
	return str(c)

lines = [line.strip() for line in open('C-small-attempt0.in.txt')]
nTest = int(lines[0])
for i in range(1,nTest+1):
	A = int(lines[i].split()[0])
	B = int(lines[i].split()[1])
	print "Case #" + str(i) + ": " + countFair(A, B)
