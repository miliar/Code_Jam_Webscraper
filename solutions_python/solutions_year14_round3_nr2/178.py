import psyco
import sys
import itertools
import re

psyco.full()

test_input = r'''3
3
ab bbbc cd
4
aa aa bc c
2
abc bcd'''.split('\n')

DEBUG = False

KNOWN = {

}

def debug(s, always=False):
	if not DEBUG and not always:
		return
	sys.stderr.write(str(s) + '\n')

def readline():
	if DEBUG:
		return test_input.pop(0)
	return raw_input()				

def solvable(cars):
	return True
	
def valid(order):
	s = ''.join(order)
	l = len(s)
	for i, c in enumerate(s):
		# Continue while same character.
		if i+1 < l and s[i + 1] == c:
			continue
		
		# Check character isn't found again later.
		if s.rfind(c) == i:
			continue
		else:
			return False
	return True
	
def case(casenum):

	_ = int(readline())
	cars = readline().split()
	
	debug(["cars (%d):" % (len(cars),), cars], True)

	output = 0
	
	if solvable(cars):
		
		n = 0
		for order in itertools.permutations(cars):
			if valid(order):
				n += 1
				
		output = n		
	
	print "Case #%d: %s" % (casenum, output)
	
	

def main():
	numcases = readline()
	for i in xrange(int(numcases)):
		case(i + 1)

main()
