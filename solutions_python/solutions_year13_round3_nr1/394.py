import sys
import math
import decimal
import re

def get_int():
	return int(sys.stdin.readline())

def get_ints():
	return [int(x) for x in sys.stdin.readline().split()]

def get_float():
	return float(sys.stdin.readline())

def get_floats():
	return [float(x) for x in sys.stdin.readline().split()]

def get_string():
	return sys.stdin.readline().split()

def get_line():
	return sys.stdin.readline()

def printnn(str):
	sys.stdout.write(str)

def sort_asc(iter):
	iter.sort()
	return iter

def sort_desc(iter):
	iter.sort(reverse=True)
	return iter

TC = get_int()

for tc in range(TC):
	all = sys.stdin.readline().split()
	name = all[0]
	nc = int(all[1])

	tf = ""
	for i in range(nc):
		tf = tf + "*"

	s = re.sub("[^aeiou]", "*", name)
	#s = name

	hm = 0
	for i in range(len(s)-nc+1):
		for j in range((i+nc),len(s)+1):
			#print s[i:j]
			x = s[i:j]
			if(tf in x):
				#print x
				hm = hm +1
	
	print "Case #%d: %d" % (tc+1, hm)
