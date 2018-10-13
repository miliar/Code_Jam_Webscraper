#!/usr/bin/python
# -*- coding: utf-8 -*-


def open_fi(fi):
	fi = open(fi)
	T = int(fi.readline()[:-1])
	
	for k in xrange(T):
		N, M = map(int, fi.readline().split())
		tab = []
		for i in xrange(N):
			ch = fi.readline()[:-1].split("/")[1:]
			for ii, kk in enumerate(ch):
				path = "/".join(_ for _ in ch[:ii]) + "/%s" %kk
				if path not in tab:
					tab.append(path)
		
		tot = 0
		for j in xrange(M):
			ch = fi.readline()[:-1].split("/")[1:]
			# print "ch", ch, j
			for ii, kk in enumerate(ch):
				path = "/".join(_ for _ in ch[:ii]) + "/%s" %kk
				if path not in tab:
					tab.append(path)
					tot += 1
		
		char = "Case #%d: %s" %(k+1, tot)
		print char
	
	fi.close()


if __name__ == "__main__":
	open_fi("A-large.in")