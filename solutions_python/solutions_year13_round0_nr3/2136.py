import sys
from math import *

def reverse_number(n, partial=0):
    if n == 0:
        return partial
    return reverse_number(n / 10, partial * 10 + n % 10)

def palindrome(n):
	return reverse_number(n) == n

if __name__=='__main__':
	f = open(sys.argv[1], 'r')
	T = int(f.readline()[:-1])
	for case_no in range(1, T + 1):
		A, B = map(int, f.readline()[:-1].split())

		a = int(ceil(sqrt(A))) if A > 0 else 0
		b = int(sqrt(B)) + 1

		S = [x**2 for x in range(a, b)]

		C = 0
		for x in S:
			if palindrome(x) and palindrome(int(sqrt(x))):
				C += 1
		print "Case #%s: %s" % (case_no, C)
	
