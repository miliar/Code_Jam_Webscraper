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

pregen = [0]

for i in xrange(1, 2000010):
    s = str(i)
    pregen.append(filter(lambda t: t < i, map(lambda j: int(s[j:] + s[:j]), xrange(len(s)))))

case_number = readint()
for case in xrange(case_number):
    A, B = readlinearray()
    print "Case #%s: %s" % (case + 1, sum(map(lambda i: len(filter(lambda j: j >= A, pregen[i])), xrange(A, B+1))))
