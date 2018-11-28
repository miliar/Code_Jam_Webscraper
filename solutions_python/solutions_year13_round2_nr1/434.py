#!/usr/bin/python
from heapq import heappush, heappop


T = input()

def add_mote(m, M):
    heappush(M, m)

def remove_mote(M):
	return heappop(M)




for case in range(1, T + 1):
	A, N = [int(i) for i in raw_input().split()]
	mote = A
	if mote == 1:
		print "Case #%d: %d" % (case, N)
		raw_input()
		continue
	non_absorbvable = []
	for s in raw_input().split():
		s = int(s)
		add_mote(s, non_absorbvable)
		#print s, mote
		#print non_absorbvable, s, mote
		while len(non_absorbvable) > 0 and mote > non_absorbvable[0]:
			mote = mote + remove_mote(non_absorbvable)
	count = 0
	if len(non_absorbvable) > 0:
		#print non_absorbvable
		while len(non_absorbvable) > 0:
			delta = 0
			#print non_absorbvable
			while mote <= non_absorbvable[0]:
				mote = mote * 2 - 1
				delta = delta + 1
			if delta >= len(non_absorbvable):
				count += len(non_absorbvable)
				break
			else:
				count = count + delta

			while len(non_absorbvable) > 0 and mote > non_absorbvable[0]:
				mote = mote + remove_mote(non_absorbvable)
			
			#if len(non_absorbvable) <= 2:
			#	count = count + len(non_absorbvable)
			#	break
		
			
	if count > N:
		count = N
	
	
	print "Case #%d: %d" % (case, count)



