#!/usr/bin/env python
import sys

map = {
	'w': [0],
	'e': [1,6,14],
	'l': [2],
	'c': [3,11],
	'o': [4,9,12],
	'm': [5,18],
	' ': [7,10,15],
	't': [8],
	'd': [13],
	'j': [16],
	'a': [17],
}

def parseresult(result):
	return "{0:0>4d}".format(result%10000)

def parsecase(string):
	tab = [1]

	for i in range(19):
		tab += [0]
	
	for letter in string:
		if letter in map:
			for i in map[letter]:				
				tab[i+1] += tab[i]
				tab[i+1] %= 10000
	
	return tab[19]

def parseinput():
	n = sys.stdin.readline()
	j=1
	for i in sys.stdin:
		k = parsecase(i)
		print "Case #{0}: {1}".format(j,parseresult(k))
		j+=1

parseinput()
