#!/usr/bin/python

import sys

if len(sys.argv) < 2:
	print "oops"
	sys.exit(1)

def allPrimes(b, p):
	primes = [2, 3]
	for i in range(3, b, 2):
		isPrime = 1
		for x in primes:
			if i % x == 0:
				isPrime = 0
				break
		if isPrime:
			primes.append(i)
	for i in range(len(primes)):
		if primes[i] >= p:
			return primes[i:]

def getParent(uf, i):
	if(uf[i] == -1):
		return i
	else:
		uf[i] = getParent(uf, uf[i])
		return uf[i]

def join(uf, i, j):
	iP = getParent(uf, i)
	jP = getParent(uf, j)
	if iP == jP:
		return 0
	else:
		uf[iP] = jP
		getParent(uf, iP)

def sharesFactor(a, b):
	i, j = 0, 0
	while i < len(a) and j < len(b):
		if a[i] == b[j]:
			return 1
		elif a[i] > b[j]:
			j += 1
		else:
			i += 1
	return 0

f = open(sys.argv[1], "r")

numCases = int(f.readline())

for i in range(numCases):
	line = f.readline().split()
	A = int(line[0])
	B = int(line[1])
	P = int(line[2])
	
	groups = []
	primes = allPrimes(B, P)
	
	for x in range(A, B + 1):
		tmp = []
		for t in primes:
			if x % t == 0:
				tmp.append(t)
		groups.append(tmp)
	
	uf = []

	for j in range(len(groups)):
		uf.append(-1)
	
	change = 1

	while change:
		change = 0
		for j in range(len(groups) - 1):
			for k in range(j + 1, len(groups)):
				if sharesFactor(groups[j], groups[k]):
					change = change or join(uf, j, k)
	r = 0

	for j in uf:
		if j == -1:
			r += 1
	
	print "Case #" + str(i + 1) + ": " + str(r)
