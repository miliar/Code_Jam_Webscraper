#!/usr/bin/python
#
# Google Code Jam
#
#

import sys
import os
from collections import deque
from operator import itemgetter

debug=False


def solve_test_case(input):
	I = input.readline().strip().split()
	I.reverse()

	combine = {}
	c = int(I.pop())
	while c > 0:
		s = list(I.pop())
		combine[(s[0], s[1])] = s[2]
		combine[(s[1], s[0])] = s[2]
		c -= 1
		
	opposed = {}
	c = int(I.pop())
	while c > 0:
		s = list(I.pop())
		opposed[s[0]] = s[1]
		opposed[s[1]] = s[0]
		c -= 1

	I.pop()
	s = list(I.pop())
	r = []
	for e in s:
		if len(r) == 0:
			r.append(e)
		elif (r[-1], e) in combine:
			ne = combine[(r[-1], e)]
			r.pop()
			r.append(ne)
		elif e in opposed and opposed[e] in r: 
			r = []
		else:
			r.append(e)
			
	return "[%s]" % ", ".join(r)

def fast_pow(x, n):
        global cache
        if n == 0: return 1
        if (x,n) in cache: return cache[(x,n)]
        if (n & 1):
                a = fast_pow(x, (n-1) >> 1)
                r = x * a * a
        else:
                a = fast_pow(x, n >> 1)
                r = a * a
        cache[(x,n)] = r
        return r

def dotProduct(v1,v2):
	return reduce(lambda p,(x,y):p + x*y, zip(v1,v2))

def crossProduct((x1,y1),(x2,y2)):
	return x1*y2 - y1*x2

def strToBase(s, base):
	return reduce(lambda x,y: x*base+y, map(int,s))

		
primes = []

def next_prime(seq):
	global primes
	discards = set()
        it = iter(seq)
	while True:
		x = it.next()
		for p in primes: discards.add(p*x)
		if not x in discards: 
			primes.append(x)
			discards.add(x*x)
			yield x

def integersFrom2():
	i = 2
	while True: 
		yield i
		i += 1

prime_gen = next_prime(integersFrom2())


binomials = {}

def choose(x,n):
        global binomials
        if x == 0: return 0
        if n == 0: return 1
        if (x,n) in binomials: return binomials[(x,n)]
        r = choose(x-1,n-1) + choose(x-1,n)
        binomials[(x,n)] = r
        return r

def gcd(a,b):
	while b != 0:
		a, b = (b, a%b)
	return a

def lcm(a,b):
	return a*(b/gcd(a,b))



if __name__ == '__main__':
	input = open(sys.argv[1])
	if len(sys.argv) > 2 and sys.argv[2] == "--debug": debug=True
	test_case_count = int(input.readline().strip())
	test_case = 0
	while test_case < test_case_count:
		test_case += 1
		print "Case #%d: %s" % (test_case, solve_test_case(input))


 
            
 
