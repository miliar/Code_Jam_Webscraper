#!/usr/bin/python
# -*- coding: utf-8 -*-
## Problem A. Bot Trust (GCJ Qualif 2011)


def open_fi(fi):
	fi = open(fi)
	T = int(fi.readline()[:-1])
	newfi = open("A-large.out", "w")
	
	for k in xrange(T):
		#print k+1, "*"*10
		ent = fi.readline().split()
		N = int(ent.pop(0))
		#print ent
		
		player = [1]*2
		nplay, autre = 0, 1
		if ent[0] == "B":
			nplay, autre = 1, 0
		mem, chgt = 0, 0
		sol = 0 ## solution
		for h in ent:
			if h == "O":
				if nplay != 0:
					chgt = 1
				else:
					chgt = 0
				nplay, autre = 0, 1
			elif h == "B":
				if nplay != 1:
					chgt = 1
				else:
					chgt = 0
				nplay, autre = 1, 0
			else:
				a = int(h)
				b = a - player[nplay]
				pas = max(abs(b) - mem*chgt, 0)
				if b > 0:
					sol = sol + pas # move forward
				elif b < 0:
					sol = sol + pas # move backward
				sol += 1 ## push
				player[nplay] = a # move
				if chgt == 1:
					mem = 0
				mem = mem + pas + 1
				
				#print player, b, mem, chgt, pas, sol
				
		
		char = "Case #%d: %s" %(k+1, sol)
		newfi.write(char)
		if k <= T:
			newfi.write("\n")
		print char
	
	newfi.close()
	fi.close()


if __name__ == "__main__":
	open_fi("A-large.in")
	