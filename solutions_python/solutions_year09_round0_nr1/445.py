#!/usr/bin/env python
# -*- coding: utf8 -*-
# Johan Musaeus Bruun, 20090903

import sys

def main(fin):
	L, D, N = map(int, fin.readline().split())
	# L = word length, D = num words, N = num cases/patterns
	wordlist = readnlines(fin,D)
	
	for case in range(N):
		pattern = trimn(fin.readline())
		pattern = splitpattern(pattern)
		validwords = numvalid(wordlist,pattern)
		print "Case #%d: %d" % (case+1, validwords)
		
	exit()


def numvalid(wordlist,pattern):
	validwords = 0
	for word in wordlist:
		validwords = validwords + validate(word,pattern)
	return validwords


def validate(word,pattern):
	for i, v in enumerate(word):
		if v not in pattern[i]:
			return 0
	return 1


def splitpattern(pattern):
	arr = ['' for i in xrange(len(pattern))]
	arrindex = 0
	inside = False
	for v in pattern:
		if v=='(':
			inside = True
		elif v==')':
			inside = False
			arrindex = arrindex + 1
		else:
			if inside==True:
				arr[arrindex] = arr[arrindex] + v
			else:
				arr[arrindex] = v
				arrindex = arrindex + 1
	arr = [x for x in arr if x != '']
	return arr


def readnlines(fin,n):
	l = ['' for i in xrange(n)]
	for i in xrange(n):
		l[i] = trimn(fin.readline())
	return l


def trimn(s):
	#return (s[-1] == '\n') ? s[:-1] : s
	if len(s) > 1 and s[-1] == '\n':
		return s[:-1]
	else:
		return s

def trimns(l):
	for i in xrange(len(l)):
		l[i] = trimn(l[i])
	return l

################################################################

if __name__ == '__main__':
	try:
		inputfile = "A-test.in" #"A-small-practice.in"
		#fin = open(inputfile, 'r')
		fin = sys.stdin 
		main(fin)
	except IOError:
		print "File I/O error!"
