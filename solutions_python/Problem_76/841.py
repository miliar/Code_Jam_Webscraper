#!/usr/bin/env python
#coding=utf-8

import sys

m = []
r = []
size = 0

result = 0

def subset(set, pos):
	global result
	if pos < size:
		for n in range(len(set)):
			r[pos] = set[n]
			#
			t1 = r[:pos+1]
			t2 = m[:]
			[t2.remove(x) for x in t1]
			#print t1, t2
			s1, s2 = t1[0], t2[0] 
			for x in t1[1:]:
				s1 = s1 ^ x
			for x in t2[1:]:
				s2 = s2 ^ x
			if s1 == s2:
				s = sum(t1)
				if s > result:
					result = s
				s = sum(t2)
				if s > result:
					result = s
			#
			subset(set[n+1:],pos+1)

fi = file(sys.argv[1])
fo = file("a.output", "w")

Ncase = int(fi.readline())

for nc in range(Ncase):
	Nm = int(fi.readline())
	m = [int(x) for x in fi.readline().split("\n")[0].split()]
	print m

	size = len(m) / 2
	r = m[:]
	#print r

	result = 0
	subset(m, 0)

	if result > 0:
		print "Case #%d: %d" % (nc+1, result)
		fo.write("Case #%d: %d\n" % (nc+1, result))
	else:
		print "Case #%d: NO" % (nc+1,)
		fo.write("Case #%d: NO\n" % (nc+1,))

	#print "Case #%d: %s" % (nc+1, r)
	#fo.write("Case #%d: %s\n" % (nc+1, r))

fi.close()
fo.close()
