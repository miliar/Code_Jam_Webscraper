# Fair and Square
# Google Code Jam 2013
# Andrew Tarzwell
# April 12 2013

import sys
import math

cases = []

def get_data():
	n = int(sys.stdin.readline())
	for c in xrange(n):
		line = sys.stdin.readline()
		i = [int(x) for x in line.split(" ")]
		i[1] = i[1] + 1
		cases.append(i)

def is_palindrome(num):
	s = str(num)
	#print "str: " + s
	sz = int(len(s)/2)
	#print "sz: " + str(sz)
	if sz != 0:
		for c in xrange(sz):
			if s[c] != s[len(s) - c - 1]:
				return False
			else:
				return True
	else: return True

	
def solve(case):
	fs = 0 #num of fair and square numbers
	for x in xrange(*case):
		rpal = False #Roots are palindromes
		sq = False #Square number
		pal = is_palindrome(x)
		if pal:
			sq = math.sqrt(x)
			isq = int(sq)
			#print x
			if isq*isq == x:
				if is_palindrome(isq):
					fs += 1
					#print x
	return str(fs)

if __name__ == "__main__":
	get_data()
	for idx, case in enumerate(cases):
		print "Case #" + str(idx+1) + ": " + solve(case)	
		#solve(case)	
