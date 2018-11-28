from re import *
from sys import stderr
def readint():
	return int(raw_input())
def readfloat():
	return float(raw_input())
def readarray(N, foo=raw_input):
	return [foo() for i in xrange(N)]
def readlinearray(foo=int):
	return map(foo, raw_input().split())

def NOD(a, b):
	while b:
		a,b = b, a%b
	return a

def gen_primes(max):
	primes = [1]*(max+1)
	for i in range(2, max+1):
		if primes[i]:
			for j in range(i+i, max+1, i):
				primes[j] = 0
	primes[0] = 0
	return [x for x in range(max+1) if primes[x]]

def is_prime(N):
	i = 3
	if not(N % 2):
		return 0
	while i*i < N:
		if not(N % i):
			return 0
		i += 3
	return 1

import operator

#x = [0]*1010
#y = [0]*1010

#for i in xrange(2, 1001):
	#y[i] = 2.0 * sum(y[:i]) / float(i - 1) + 1.0
#for i in xrange(2, 1001):
	#x[i] = y[i] + 1.0
#print y
x = [1] * 1001
x[0] = x[1] = 0

case_number = readint()
for case in xrange(case_number):
	N = readint()
	seq = readlinearray()
	result = N - len(filter(lambda n: n + 1 == seq[n], range(N)))
	print "Case #%s: %s" % (case + 1, result)
