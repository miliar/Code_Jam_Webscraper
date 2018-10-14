#!/usr/bin/env python
#coding=utf-8

import sys


def check(ma, start):
    ret = True
    mb = ma[:]
    mc = mb[start:]
    mc.sort()
    mb[start:] = mc
    for l in range(start,len(mb)):
        if mb[l] > l:
            ret = False
            break
    #print "Check", start, ret
    return ret

fi = file(sys.argv[1])
fo = file("a.output", "w")

Ncase = int(fi.readline())

for nc in range(Ncase):
	m = fi.readline().split("\n")[0]
	t = m.split()
	Nm = int(t[0])
	c = t[1:]
	print Nm, c

	(Oc, Oas, Bc, Bas, a) = (1, 0, 1, 0, 0)
	for n in range(Nm):
		if c[n*2] == 'O':
			On = int(c[n*2+1])
			Os = abs(On - Oc)
			if Os > Bas:
				a += Os - Bas + 1
				Oas += Os - Bas + 1
			else:
				a += 1
				Oas += 1
			print Oas, Bas, a

			Oc = On
			Bas = 0
		if c[n*2] == 'B':
			Bn = int(c[n*2+1])
			Bs = abs(Bn - Bc)
			if Bs > Oas:
				a += Bs - Oas + 1
				Bas += Bs - Oas + 1
			else:
				a += 1
				Bas += 1
			print Oas, Bas, a

			Bc = Bn
			Oas = 0
		#print n,a
	print "Case #%d: %d" % (nc+1, a)
	fo.write("Case #%d: %d\n" % (nc+1, a))

fi.close()
fo.close()
