#!/usr/bin/python

import sys

#gs=[("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand"), ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"), ("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")]
mapping={'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
#for g,e in gs:
#	for i in range(0, len(g)):
#		if g[i] == ' ':
#			continue
#		else:
#			mapping[g[i]] = e[i]
f=open(sys.argv[1])
tc=int(f.readline().strip())
for i in range(1,tc+1):
	mapped=" ".join(["".join([mapping[c] for c in word]) for word in f.readline().strip().split()])
	print "Case #%d: %s" % (i,mapped)

