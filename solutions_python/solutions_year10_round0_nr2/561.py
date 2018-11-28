#!/usr/bin/python

def gcd (x, y):
	if y == 0: return x
	return gcd(y, x%y)

nT = int(raw_input())
for T in range(1,nT+1):
	ent = raw_input()
	e = ent.split(' ')
	sz = int(e[0])
	mdc = max(int(e[1]), int(e[2]))-min(int(e[1]),int(e[2]))
	for i in range(1, sz+1):
		for j in range(i+1, sz+1):
			mdc = gcd(mdc, max(int(e[i]), int(e[j]))-min(int(e[i]),int(e[j])))
	if int(e[1])%mdc == 0:
		print "Case #%d: 0" % T
	else: print "Case #%d: %d" % (T, mdc-int(e[1])%mdc)

