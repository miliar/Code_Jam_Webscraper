#!/usr/bin/env python

def solve(B, O, seq):
	Bpos = 1
	Opos = 1
	sec = 0
	pushed = False

	while (len(B) > 0 or len(O) > 0):
		if B != []:
			if B[0] < Bpos:
				Bpos -= 1
			elif B[0] > Bpos:
				Bpos += 1
			elif B[0] == Bpos and seq[0] == 'B':
				del B[0]
				pushed = True
		if O != []:
			if O[0] < Opos:
				Opos -= 1
			elif O[0] > Opos:
				Opos += 1
			elif O[0] == Opos and seq[0] == 'O':
				del O[0]
				pushed = True

		if pushed:
			del seq[0]
			pushed = False
		sec += 1
	return sec


T = int(raw_input().strip())

Op = []
Bp = []
sequence = []
Bpos = 1
Opos = 1

for t in range(T):
	line = raw_input().strip().split()
	N = int(line[0])
	del line[0]
	for x in range(N):
		x *= 2
		
		if line[x] == 'O':
			Op.append(int(line[x+1]))
		elif line[x] == 'B':
			Bp.append(int(line[x+1]))
		sequence.append(line[x])
		
	print "Case #%d: %d" % (t+1, solve(Bp, Op, sequence))

	Bp = []
	Op = []
	sequence = []


