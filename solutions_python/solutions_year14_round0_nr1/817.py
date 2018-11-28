#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def magic_trick(t):
	first = int(t[0])
	second = int(t[5])
	set1 = t[first].split(" ")
	set2 = t[second+5].split(" ")
	cands = []
	for k in xrange(0, 4):
		if set1[k] in set2:
			cands.append(set1[k])
	if cands == []:
		return "Volunteer cheated!"
	elif len(cands) > 1:
		return "Bad magician!"
	else:
		return cands[0]

if __name__ == "__main__":
	with open(sys.argv[1]) as f:
		buf = f.read()
	t = buf.split("\n")
	nb_boards = int(t[0])
	t = t[1:]
	for k in xrange(0, nb_boards):
		print "Case #%d: %s"%(k+1, magic_trick(t[k*10:k*10+10]))
