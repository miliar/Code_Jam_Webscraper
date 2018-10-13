#!/usr/bin/python
from math import *
import sys

ranges = [];

def run():
	#assume well formed input
	testcases = int(sys.stdin.readline());
	for i in range(testcases):
		line = sys.stdin.readline();
		testcase(i+1, long(line.split()[0]), long(line.split()[1]));

def testcase(tc, lower, upper):
	global ranges;
	count = 0;
	lr = int(ceil(sqrt(lower)));
	ur = int(floor(sqrt(upper)));

	for r in ranges:
		if r[0] >= lr and r[1] <= ur:
			count += countfas(lr, r[0] - 1);
			count += r[2];
			count += countfas(r[1] + 1, ur);

			break;
	if count == 0:
		count = countfas(lr, ur);

	print "Case #"+str(tc)+":", count;

def countfas(lr, ur):
	global ranges;
	count = 0;
	for n in palindromes(lr, ur):
		if (ispalindrome(n**2)):
			count += 1;
	ranges += [(lr, ur, count)];
	return count;

def ispalindrome(n):
	s = str(n);
	l = len(s);
	for i in xrange(l/2):
		if(s[i] != s[l - 1 - i]):
			return False;
	return True;


def palindromes(lower, upper):
	if ispalindrome(lower):
		p = lower;
	else:
		#generate palindrome closest to lower.
		p = makepalindrome(lower);
		if (p < lower):
			p = nextpalindrome(lower);
	
	while (p <= upper):
		yield p;
		p = nextpalindrome(p);

# forces number into a palindrome by taking the first n digits and repeating them in reverse order.
def nextpalindrome(p):
	s = str(p);
	l = len(s);

	firsthalf = s[0:l / 2 + l % 2];
	f = long(firsthalf) + 1;

	return makepalindrome(long( str(f) + '0'*(l/2)));

# makes a number into a palindrome (which may be less than the original number!!!)
def makepalindrome(n):
	s = list(str(n));
	l = len(s);
	for i in xrange(l/2+1):
		s[l-i-1] = s[i];
	return long(''.join(s));


if __name__ == "__main__":
	run();
