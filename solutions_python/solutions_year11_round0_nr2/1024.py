#!/usr/bin/env python
#coding=utf-8

import sys

fi = file(sys.argv[1])
fo = file("a.output", "w")

Ncase = int(fi.readline())

for nc in range(Ncase):
	m = fi.readline().split("\n")[0].split()
	print m

	i = 0
	c = {}
	o = []

	Nc = int(m[i])
	i += 1
	if Nc > 0:
		for n in range(Nc):
			c[(m[i][n*3],m[i][n*3+1])] = m[i][n*3+2]
			c[(m[i][n*3+1],m[i][n*3])] = m[i][n*3+2]
		i += 1

	Nd = int(m[i])
	i += 1
	if Nd > 0:
		for n in range(Nd):
			o.append((m[i][n*2],m[i][n*2+1]))
			o.append((m[i][n*2+1],m[i][n*2]))
		i += 1

	Nn = int(m[i])
	i += 1

	s = m[i]

	#print c, o, s

	r = [s[0]]
	for n in range(1, Nn):
		# comb
		r.append(s[n])
		if(len(r) < 2):
			continue
		if((r[-1], r[-2]) in c):
			r[-2] = c[(r[-1],r[-2])]
			r.pop()
		#print "comb:", r
		# opp
		for x in range(len(r)):
			if((r[x],r[-1]) in o):
				r = []
				break
		#print "opp:", r

	print "Case #%d: %s" % (nc+1, r)
	fo.write("Case #%d: %s\n" % (nc+1, r))

fi.close()
fo.close()
