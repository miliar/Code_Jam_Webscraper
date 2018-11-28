# Angel Sancho <angelitodeb@gmail.com>
# 
# Google Code Jam 2012 - Qualification Round - A. Speaking In Tongues

import sys

eng = ["q", "a zoo", "our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"]
goo = ["z", "y qee", "ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]

tr = {}

for i in range (0, len(eng)):
	for j in range (0, len(eng[i])):
		tr[goo[i][j]] = eng[i][j]

fp = open(sys.argv[1])

T = int(fp.readline().strip())

for c in range(T):
	a = fp.readline().strip()
	b = ""

	for i in range(0, len(a)):
		b = b+tr[a[i]]

	print "Case #%d: %s" % ((c+1), b)
