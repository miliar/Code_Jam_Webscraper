#!/usr/bin/env python

import gmpy2

def main():
	#print 'Fair and Square'

	#print is_palindrome(100)

	#print solve(1, 4)
	#print solve(10, 120)
	#print solve(100, 1000)

	#print solve(1,10**100)

	with open('c:\Users\Kornelijus\Downloads\C-small-attempt0.in', 'r') as f:
		count = int(f.readline())

		for i in xrange(count):
			a, b = f.readline().split(' ')
			count = solve(gmpy2.mpz(a), gmpy2.mpz(b))
			print 'Case #%d: %d' % (i + 1, count)

def is_palindrome(n):
	r = gmpy2.mpz()
	num = gmpy2.mpz(n)

	while num > 0:
		r = r * 10 + num % 10
		num /= 10

	return n == r


def ispalindrome(num):
    z = num.digits(10) 
    return z==z[::-1]
    #return 0  
 	#digits = gmpy2.num_digits(num, 10)
 	#opa = gmpy2.t_div(num, gmpy2.mpz(10) ** gmpy2.mpz(digits - 22))
 	#cya = gmpy2.f_mod(num, 10 ** 22)

 	#return opa.digits() == cya.digits()

def solve(a, b):
	startx = gmpy2.isqrt_rem(a)
	endx = gmpy2.isqrt_rem(b)

	start = startx[0] if startx[1] == 0 else startx[0] + 1
	end = gmpy2.mpz(endx[0])

	tja = 0

	ye = gmpy2.mpz(start)
	while ye <= end:
		if ispalindrome(ye) and ispalindrome(ye * ye):
			tja += 1
		ye += 1

	return tja


if __name__ == '__main__':
	main()
