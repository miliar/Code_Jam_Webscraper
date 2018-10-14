#!/usr/bin/env python

# precalculated answers, solved using pen & paper.
data = """
n = 1
T
TT
TTT
TTTT

n = 2
F
TT
FTF
TTTT

n = 3
F
FF
FTT
FFTF

n = 4
F
FF
FFF
FFTT
"""

precalc = data.split('\n')
#print precalc

TC = int(raw_input().strip())
for tc in xrange(1, TC + 1):
	print "Case #%d:" % tc, 
	X, R, C = map(int, raw_input().strip().split())
	if C > R:
		R, C = C, R
	answer = precalc[(X - 1) * 6 + 2 + R - 1][C - 1]
	if answer == 'T':
		print "GABRIEL" 
	else:
		print "RICHARD"
