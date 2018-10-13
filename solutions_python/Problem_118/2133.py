#!/usr/bin/python
import math
from sys import argv
def sqrtest(n):
	root = math.sqrt(n)
	r = str(root)[::-1]
	if r[1] == '.':
		return True
	return False

def palindrome(foo):
	t = str(foo)
	if t[::-1] == t:
		return True
	return False

fin = open(argv[1])
flag = True
numcount = 0
casecount = 1

for line in fin:
	if flag:
		flag = False
		continue
	f = line.strip()
	f = f.split()
	t = tuple(f)
	a,b = t
	for i in range(int(b)):
		if i < int(a)-1:
			continue
		if sqrtest(i+1):
			if palindrome(i+1):
				if palindrome(int(math.sqrt(i+1))):
					numcount += 1
	print 'Case #'+str(casecount)+':', numcount
	casecount+=1
	numcount = 0
