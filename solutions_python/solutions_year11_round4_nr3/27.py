#!/usr/bin/python -OO

import sys;
import math;

def readia():
	return [int(x) for x in sys.stdin.readline().strip().split()];
def readsa():
	return sys.stdin.readline().strip().split();
def readi():
	return int(sys.stdin.readline().strip());
def reads():
	return sys.stdin.readline().strip();
def perr(s):
	print >>sys.stderr, s;

def nod(a, b):
	while a % b > 0:
		c = a % b;
		a = b;
		b = c;
	return b;

def nok(a, b):
	return a * b / nod(a, b);

def getPrimes():
	primes = [2];

	i = 3;
	while i < 10000:
		prime = True;
		for p in primes:
			if p*p > i:
				break;
			if i % p == 0:
				prime = False;
				break;
		if prime:
			primes.append(i);
		i += 2;
	return primes;

primes = getPrimes();

def factorize(a):
	numPrimes = 0;
	for p in primes:
		if p*p > a:
			break;
		while a % p == 0:
			numPrimes += 1;
			a /= p;
			if a == 1:
				break;
	if a != 1:
		numPrimes += 1;

	return numPrimes;

def main():
	T = readi();
	for t in range(T):
		n = readi();
		nums = [];
		noks1 = [];
		prevNok = 0;
		curNok = 1;
		numNoks1 = 0;
		for i in xrange(1, n+1): 
			curNok = nok(curNok, i);
			#noks1.append(curNok);
			if curNok != prevNok:
				numNoks1 += 1;
				noks1.append((i, curNok));
				prevNok = curNok;
		#print numNoks1, ": ", noks1;
		noks2 = [];
		prevNok = 0;
		curNok = 1;
		numNoks2 = 0;
		for p in primes:
			if p <= n:
				numNoks2 += 1;
			else:
				break;
		#print numNoks2;
		if n == 1:
			numNoks2 = 1;
		print "Case #%d: %d" % (t + 1, abs(numNoks1 - numNoks2));




main();
