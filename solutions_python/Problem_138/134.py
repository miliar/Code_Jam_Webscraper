#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
# google code jam - c.durr- 2014

# Deceitful War
# https://code.google.com/codejam/contest/2974486/dashboard#s=p3
# simulation
 
def readint():    return int(raw_input())
def readarray(f): return map(f, raw_input().split())

def deceitfulWar(N,K):
	j     = 0
	score = 0
	for ni in N:
		if ni<K[j]:
			# Noemi looses
			pass
		else:
			# Noemi wins
			score += 1
			j += 1
	return score

def war(N,K):
	j = len(K)-1
	score = 0
	for ni in N[::-1]:
		if ni<K[j]:
			# Noemi looses
			j -= 1
		else:
			# Noemi wins
			score += 1
	return score

for test in range(readint()):
	nbBlocs = readarray(int)
	N = readarray(float)
	K = readarray(float)
	N.sort()
	K.sort()
	print "Case #%i:"% (test+1), deceitfulWar(N,K), war(N,K)
