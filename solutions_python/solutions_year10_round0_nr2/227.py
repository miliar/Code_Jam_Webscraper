
import os, sys, re

def SWAP(a, b):
	return b, a

def GCD(a, b):
	if a < b:
		[a, b] = SWAP(a, b)
	
	while(b > 0):
		a %= b
		[a, b] = SWAP(a, b)
	
	return a

FN = sys.argv[1]

f = open(FN, 'r')

ncase = int(f.readline())

for idx in range(1, ncase + 1):

	line = f.readline()

	items = line.split()

	del items[0]

	bnum = long(items[0])

	del items[0]

	G = abs(long(items[0]) - bnum)

	del items[0]

	for item in items:

		G = GCD(abs(long(item) - bnum), G)
	
	ret = (G - bnum % G) % G

	print "Case #%d: %ld" %(idx, ret)
	

# vim: ts=2 sw=2
