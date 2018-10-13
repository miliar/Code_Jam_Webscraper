import sys
from math import sqrt

DEBUG = 0
rl = sys.stdin.readline

def strings_to_ints(str):
	return [int(num) for num in str.strip().split(' ')]

def fair(number):
	s = str(number)
	if s == s[::-1]: return True
	return False

def fair_and_square(number):
	if DEBUG:
		print "%d (%f ** 2): F:%s Dec:%s FSqr:%s" % (number, sqrt(number), fair(number), int(sqrt(number)) == number, fair(int(sqrt(number))))
	if fair(number) and int(sqrt(number)) == sqrt(number) and fair(int(sqrt(number))): return True
	return False

def solve(start, end):
	fas = []
	for i in xrange(start, end+1):
		if fair_and_square(i): fas += [i]
	return len(fas)

def main():
	numcases = int(rl())
	for case in xrange(1, numcases+1):
		start, end = strings_to_ints(rl())
		outcome = solve(start, end)
		print "Case #%d: %s" % (case, outcome)

if __name__ == '__main__':
	main()