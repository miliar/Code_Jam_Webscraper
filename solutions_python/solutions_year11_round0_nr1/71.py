#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division

import sys

T = int(raw_input())

for t in range(1, T + 1):
	xs = raw_input().split()
	N = int(xs[0])
	ns = xs[1:]
	Ocommands = []
	Bcommands = []
	fullorder = []
	for n in range(N):
		if xs[2*n+1] == "O":
			Ocommands.append(int(xs[2*n+2]))
		elif xs[2*n+1] == "B":
			Bcommands.append(int(xs[2*n+2]))
		fullorder.append((xs[2*n+1], int(xs[2*n+2])))
		# print "  ", xs[2*n+1], xs[2*n+2]
	Opos = 1
	Bpos = 1
	timestep = 0
	while len(Ocommands) > 0 or len(Bcommands) > 0:
		# print timestep, Ocommands, Bcommands, fullorder, Opos, Bpos
		havepushed = False
		if len(Ocommands) > 0:
			if Opos == Ocommands[0] and fullorder[0] == ("O", Ocommands[0]) and not havepushed:
				Ocommands = Ocommands[1:]
				fullorder = fullorder[1:]
				havepushed = True
			elif Opos < Ocommands[0]:
				Opos += 1
			elif Opos > Ocommands[0]:
				Opos -= 1
		if len(Bcommands) > 0:
			if Bpos == Bcommands[0] and fullorder[0] == ("B", Bcommands[0]) and not havepushed:
				Bcommands = Bcommands[1:]
				fullorder = fullorder[1:]
				havepushed = True
			elif Bpos < Bcommands[0]:
				Bpos += 1
			elif Bpos > Bcommands[0]:
				Bpos -= 1
		timestep += 1
	print "Case #%d: %s" % (t, timestep)
