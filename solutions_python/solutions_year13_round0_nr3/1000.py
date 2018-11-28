import sys
import math

n = 0

filename = sys.argv[1]

def is_palindrome(num):
	s = str(num)
	return s == s[::-1]

def process_case(a, b):

	lo = int(math.sqrt(a))
	hi = int(math.sqrt(b))

	cnt = 0

	for i in xrange(lo, hi + 1):
		num = i ** 2
		if num >= a and num <= b and is_palindrome(num) and is_palindrome(i):
			#print '{2} and {3}: [{4} and {5}]: {0} ^ 2 = {1}'.format(i, num, a, b, lo, hi)
			cnt += 1
	return cnt

with open(filename) as f:
	n = int(f.readline().strip())
	for casenum in xrange(n):
		a, b = map(int, f.readline().strip().split(' '))
		print 'Case #{0}: {1}'.format(casenum + 1, process_case(a, b))
