#!/usr/bin/python
# -*- coding: utf-8 -*-


def open_fi(fi):
	fi = open(fi)
	T = int(fi.readline()[:-1])
	
	for k in xrange(T):
		N = int(fi.readline())
		y = 0
		tab = [map(int, fi.readline().split()) for _ in xrange(N)]
		
		for i, ch in enumerate(tab):
			a, b = ch
			chn = tab[0:i] + tab[i+1:]
			for nj in chn:
				aa, bb = nj
				if a <= aa and b >= bb:
					y += 1
		
		
		char = "Case #%d: %s" %(k+1, y)
		print char
	
	fi.close()


if __name__ == "__main__":
	open_fi("A-large.in")