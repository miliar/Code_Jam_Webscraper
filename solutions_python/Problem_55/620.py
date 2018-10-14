#!/usr/bin/python
# -*- coding: utf-8 -*-


def open_fi(fi):
	fi = open(fi)
	T = int(fi.readline()[:-1])
	newfi = open("C-small-attempt0.out", "w")
	
	
	for p in xrange(T):
		R, k, N = map(int, fi.readline().split())
		tab = map(int, fi.readline().split())
		tot = 0 ## argent
		# print R, k, N
		
		for h in xrange(R):
			max = 0 ## max passagers
			i = 0
			while max <= k and i < N:
				max += tab[i]
				i += 1
			## correction de -1 car :i => tab[i] pas inclus
			if max > k:
				## ils ne sont pas tous dedans
				i -= 1
				max -= tab[i]
			## sinon, ils sont tous dedans
			## Ajout et queue
			tot += max
			ext = tab[:i] ## tab[i] pas inclus
			tab = tab[i:] + ext ## tab[i] inclus dans tab[i:]
		
		char = "Case #%d: %d" %(p+1, tot)
		newfi.write(char)
		if p <= T:
			newfi.write("\n")
	
	
	newfi.close()
	fi.close()

if __name__ == "__main__":
	open_fi("C-small-attempt0.in")