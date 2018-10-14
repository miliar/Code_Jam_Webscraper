#!/usr/bin/python
# -*- coding: utf-8 -*-
## Problem A. Square Tiles (GCJ Round 1C 2011)


def tiles(R, C, tab):
	for i in xrange(R-1):
		#print i, tab[i], len(tab[i]), C, C-1
		for j in xrange(C-1):
			a = tab[i][j]
			b = tab[i][j+1]
			c = tab[i+1][j]
			d = tab[i+1][j+1]
			if a == "#" and b == "#" and c == "#" and d == "#":
				tab[i] = tab[i][0:j] + "/\\" + tab[i][j+2:]
				tab[i+1] = tab[i+1][0:j] + "\\/" + tab[i+1][j+2:]
	
	
	return tab


if __name__ == "__main__":
	T = int(raw_input())
	for k in xrange(T):
		R, C = map(int, raw_input().split()) ## number of rows and columns
		tab = [raw_input().split()[0] for _ in xrange(R)] ## picture
		char = "Case #%d:" %(k+1)
		print char
		
		sol = tiles(R, C, tab)
		ok = 1
		for h in sol:
			if "#" in h:
				ok = 0
				break
		if ok == 0:
			print "Impossible"
		else:
			for h in sol:
				print h
		