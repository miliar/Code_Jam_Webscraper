#!/usr/bin/python

A = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv zq"""
B = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up qz"""

M = dict()
for i, x in enumerate(A):
	M[x] = B[i]

line = raw_input()
i = 1
while True:
	try:
		line = raw_input()
		print "Case #%d: %s" % (i, "".join(M[x] for x in line))
		i += 1
	except EOFError:
		break
