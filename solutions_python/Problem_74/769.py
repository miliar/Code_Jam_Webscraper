#!/usr/bin/env python

import sys

lines = open(sys.argv[1], 'r').readlines()

N = int(lines[0])

for lnum in xrange(1, N+1):
	line = lines[lnum]
	opos = bpos = 1
	
	bits = line.rstrip().split(' ')
	N = int(bits[0])

	instructions = []
	for i in xrange(1, 2*N+1, 2):
		instructions.append((bits[i], int(bits[i+1])))
	
	I = 0
	t = 0
	while True:
		t += 1
		
		bnext = onext = 0
		for inst in instructions[I:]:
			if inst[0] == 'B' and not bnext:
				bnext = inst[1]
			elif inst[0] == 'O' and not onext:
				onext = inst[1]
			if bnext and onext:
				break

		#print "B%d->%d\tO%d->%d"%(bpos,bnext,opos,onext)
		#print inst

		complete = False
		if bpos < bnext:
			bpos += 1
		elif bpos > bnext:
			bpos -= 1
		elif instructions[I][0] == 'B':
			complete = True

		if opos < onext:
			opos += 1
		elif opos > onext:
			opos -= 1
		elif instructions[I][0] == 'O':
			complete = True

		if complete:
			I += 1

			if I == len(instructions):
				break
	print "Case #%d: %d"%(lnum, t)

