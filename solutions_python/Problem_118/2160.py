import gmpy2
from gmpy2 import mpz
import math
def is_palin(s):
	#if s not in palindromes:
		return str(s)[::-1] == str(s)
	#return palindromes[s]

f = open("input.txt")
f.readline()
i = 0
for line in f:
	a, b  = map(int, line.split())


	c = 0
	i = i + 1
	for x in xrange(a,b+1):
		if gmpy2.is_square(x):
			z = gmpy2.isqrt(x)
			if is_palin(z):
				if is_palin(x):
	#				print a
					c = c + 1
	print "Case #" + str(i) + ": " + str(c)
