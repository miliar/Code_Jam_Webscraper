#!/usr/bin/python
# -*- coding: utf-8 -*-


def open_fi(fi):
	fi = open(fi)
	T = int(fi.readline()[:-1])
	newfi = open("A-large.out", "w")
	
	for k in xrange(T):
		N, K = map(int, fi.readline().split())
		# a = bin(K)[2:]
		# b = a[-N:]
		# if "0" in b:
			# sol = "OFF"
		# else:
			# sol = "ON"
		# 
		## que du binaire...
		p = (2**N) ## (somme des 2**k, k=0..N-1) + 1
		r = K % p ## on veut (somme des 2**k, k=0..N-1) = p-1
		if p-1 == r:
			sol = "ON"
		else:
			sol = "OFF"
		
		char = "Case #%d: %s" %(k+1, sol)
		newfi.write(char)
		if k <= T:
			newfi.write("\n")
		
	newfi.close()
	fi.close()


if __name__ == "__main__":
	open_fi("A-large.in")