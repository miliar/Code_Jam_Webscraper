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

def load_primes(primes):
	for line in open("primes2", "rt"):
		primes.append(int(line.strip()));

primes = [];
load_primes(primes);

def factorize(a):
	res = dict();
	for p in primes:
		if p*p > a:
			break;
		while a % p == 0:
			if p in res:
				res[p] += 1;
			else:
				res[p] = 1;
			a /= p;
			if a == 1:
				break;
	if a != 1:
		if a in res:
			res[a] += 1;
		else:
			res[a] = 1;
	
	return sorted(list(res.iteritems()));

def getAllDivisors(a):
	fact = factorize(a);
	numPrimes = len(fact);
	total = 1;
	for f in fact:
		total *= (f[1] + 1);
	#print "total ", total, " divisors";
	pows = [0] * numPrimes;
	r = range(numPrimes);

	done = False;
	for k in xrange(total):
		cur = 1;
		for i in r:
			cur *= pow(fact[i][0], pows[i]);
		yield cur;

		#next
		carry = 1;
		for i in r:
			pows[i] += carry;
			carry = 0;
			if pows[i] > fact[i][1]:
				pows[i] = 0;
				carry = 1;
			if carry == 0:
				break;


		
	

def main():
	T = readi();
	for t in range(T):
		(n, l, h) = readia();
		freqs = readia();
		n += 1;
		freqs.append(1);
		if n != len(freqs):
			print >>sys.stderr, "error on test ", t;
		freqs.sort();
		#print freqs;
		freqsRev = reversed(freqs);
		nods = [];
		for f in freqsRev:
			if len(nods) == 0:
				nods.append(f);
			else:
				nods.append(nod(nods[-1], f));
		nods.reverse();
		#print nods;

		noks = [];
		for f in freqs:
			if len(noks) == 0:
				noks.append(f);
			else:
				noks.append(nok(noks[-1], f));
		#print noks;

		found = False;
		res = 0;
		for i in xrange(0, n-1):
			#print i, noks[i], nods[i+1];
			# try freqs[i] <= freq <= freqs[i+1];
			if freqs[i+1] < l:
				continue;
			if freqs[i] > h:
				continue;

			curNok = noks[i];
			if curNok > h:
				continue;

			curNod = nods[i+1];
			if curNod < l:
				continue;

			if curNok > curNod:
				continue;

			if curNod % curNok != 0:
				continue;

			#print "here";
			# freq must divide nod and be divisible by nok
			rest = curNod / curNok;
			
			divisors = sorted(list(getAllDivisors(rest)));
			for divisor in divisors:
				num = curNok * divisor;
				if num > h:
					break;
				if num >= l:
					found = True;
					res = num;
					break;

			if found:
				break;

		if not found:
			lastNok = noks[n-1];
			if lastNok <= h:
				if l % lastNok == 0:
					res = l;
					found = True;
				else:
					res = (l / lastNok) * lastNok + lastNok;
					found = res >= l and res <= h;


		resStr = "Case #%d: " % (t+1);
		if found:
			resStr += str(res);
		else:
			resStr += "NO";
		print resStr;


main();
