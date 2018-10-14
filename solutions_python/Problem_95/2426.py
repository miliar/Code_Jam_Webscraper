#!/usr/bin/env python

import sys

sample_in = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

sample_out= """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

googlerese = dict()

i = 0
for c in sample_in:
	googlerese[c] = sample_out[i]
	i += 1
googlerese['z'] = 'q'
googlerese['q'] = 'z'

case = 1
lines = sys.stdin.readlines()
for line in lines[1:]:
	word = ""
	for c in line:
		word += googlerese[c]
	
	print "Case #%d: %s" % (case, word.strip())
	case += 1

