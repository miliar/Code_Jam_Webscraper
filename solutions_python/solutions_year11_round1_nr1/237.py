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

case_number = readint()
for case in xrange(case_number):
	N, pd, pg = readlinearray()
	if pg == 0 or pg == 100:
		if pd == pg:
			answer = "Possible"
		else:
			answer = "Broken"
	else:
		#ok = False
		#for i in xrange(1, N+1):
			#if i * pd % 100 == 0:
				#ok = True
		#if ok:
			#answer = "Possible"
		#else:
			#answer = "Broken"
		if 100 / NOD(pd, 100) <= N:
			answer = "Possible"
		else:
			answer = "Broken"
	print "Case #%s: %s" % (case + 1, answer)
