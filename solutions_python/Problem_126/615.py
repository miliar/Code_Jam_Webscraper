#!/usr/bin/python

from math import *
import re
rvowel = re.compile(r"a|e|i|o|u")

def vowelIndex(str, start, stop):
	l = [i for i,x in enumerate(str) if x in "aeiou" and i>=start and i<stop]
	if (len(l) == 0):
		return stop
	else:
		return min(l)

def containsVowel(str, start, stop):
	for s in str[start:stop]:
		if s in "aeiou":
			return True
	return False
	

def subw(n, b, e):
	for start in range(b, e):
		for end in range(b, e):
			if (end-start >= n):
				yield (start, end)

def calculateNValue(str, n, b=0, e=None):
	if (e==None):
		e = len(str)
	if (b>=e):
		return 0
	count = 0
	for start, end in subw(max(n,1), b, e+1):
		grams = filter(lambda w: len(w)>=n, rvowel.split(str[start:end]))
		#print "word: ", str[start:end], "found ", grams
		if (len(grams)>0):
			count += 1
	return count

T = int(raw_input())
for i in range(1, T+1):
    word, n = raw_input().split(" ", 1)
    print "Case #%d: %s"%(i, calculateNValue(word, int(n)))
    #raw_input()