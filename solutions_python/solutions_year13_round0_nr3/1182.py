import math
import sys

#f = open('input.txt');
f = sys.stdin
lines = f.read().split('\n');

nb = int(lines[0])

def isPalyndrome(l):
	return l == l[::-1]

def getSquareRoot(x):
	s = math.sqrt(x)
	s = str(s)
	
	if s[-1] == '0' and s[-2] == '.':
		return s[0:len(s)-2]
	else:
		s
	
for i in range(0, nb):
	l = lines[1+i].split(' ')
	nbMin = int(l[0])
	nbMax = int(l[1])
	nbPaly = 0
	
	for x in range(nbMin, nbMax+1):
		if isPalyndrome(str(x)):
			s = getSquareRoot(x)
			if isPalyndrome(str(s)):
				nbPaly += 1
	
	print "Case #%s: %s" % (i+1, nbPaly)