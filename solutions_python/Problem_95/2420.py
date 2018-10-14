#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import maketrans

cases = [("ejp mysljylc kd kxveddknmc re jsicpdrysi", 
		"our language is impossible to understand"),
		("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"there are twenty six factorial possibilities"),
		("de kr kd eoya kw aej tysr re ujdr lkgc jv",
			"so it is okay if you want to just give up")]

googlerese = {}
for goog, engl in cases:
	for g, e in zip(goog, engl):
		if googlerese.has_key(g):
			if googlerese[g]!=e:
				print "error"
				exit
		else:
			googlerese[g]=e

googlerese['q']='z'
googlerese['z']='q'
transtab = maketrans(''.join(googlerese.keys()), ''.join(googlerese.values()))

if __name__ == "__main__":
	tests=raw_input()

	for t in range(int(tests)):
		g=raw_input()
		print "Case #%d: %s"%(t+1,g.translate(transtab))
