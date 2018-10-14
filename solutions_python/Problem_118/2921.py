#! /usr/bin/python

import re
import math

fin = open("input.in", "r")
fout = open("output.out", "w")
sout = ""

def test(num):
	if not pal(num):
		return False
	
	d = math.sqrt(num)
	i = int(d)
	if d != i:
		return False
	return pal(i)
	
def pal(num):
	s = str(num)
	l = len(s)
	
	for i in range(int(l/2)):
		if(s[i] != s[l-i-1]):
			return False
	return True


line = fin.readline()
maxcount = int(re.search("\d+", line).group(0))

for count in range(1, maxcount+1):
	sout += "Case #" + str(count) + ": "
	total = 0
	line = fin.readline()

	limits = re.split("\D+", line)
	
	limits.pop()
	limits.reverse()

	for i in range( int(limits.pop()), int(limits.pop())+1):
		if test(i):
			total += 1

	sout += str(total)
	sout += "\n"

fout.write(sout)
