#!/usr/bin/python

import sys
import os

def has_letter(words,letter):
	return letter in ''.join(words)

def findall(s,letter):
	return [j for j in range(len(s)) if s[j]==letter]

def get_tries(words,W,L):
	D = [x for x in words if len(x)==len(W)]
	tries = 0
	for letter in L:
#		print D, letter, tries
		if has_letter(D,letter):
			if letter not in W:
				tries += 1
			places = findall(W,letter)
			D = [x for x in D if findall(x,letter)==places]
	return tries

def work(words,L):
	bestword = ''
	best_tries = -1
	for W in words:
		tries = get_tries(words,W,L)
#		print W, L, tries
		if tries > best_tries:
			best_tries = tries
			bestword = W
	return bestword

if __name__ == '__main__':
	T = int(sys.stdin.readline())
	for i in xrange(T):
		N,M = map(int, sys.stdin.readline().strip().split(' '))
		words = [sys.stdin.readline().strip() for _ in xrange(N)]
		lists = [sys.stdin.readline().strip() for _ in xrange(M)]
		print 'Case #{0}: {1}'.format(i+1,' '.join(work(words,L) for L in lists))
