#! /bin/env python

import sys

buf = sys.stdin

T = int(buf.readline())

for i in range(T):
	param = buf.readline().strip()
	param = param.split(' ')
	N = int(param[0])
	turns = oran = blue = []
	for j in range(N):
		if (param[2*j+1] == 'O'):
			turns = turns + [['O', int(param[2*j+2])]]
			oran = oran + [int(param[2*j+2])]
		else:
			turns = turns + [['B', int(param[2*j+2])]]
			blue  = blue + [int(param[2*j+2])]
	res = 0
	posO = posB = 1
	for j in turns:
		if j[0] == 'O':
			dst = j[1]-posO
			res += abs(j[1]-posO)+1
			#print "O va de", posO, "a", j[1]
			posO = j[1]
			del(oran[0])
			if blue == [] or blue[0]==posB:
				#print "blue attend"
				continue
			if blue[0] > posB:
				sig = 1
			else:
				sig = -1
			#print "blue part de", posB
			if abs(dst) > abs(blue[0]-posB):
				posB = blue[0]
			else:
				posB += sig * abs(dst)
			if abs(blue[0]-posB):
				posB += abs(blue[0]-posB)/(blue[0]-posB)
			#print "blue arrive a", posB
		if j[0] == 'B':
			#print "blue va de", posB, "a", j[1]
			dst = j[1]-posB
			res += abs(j[1]-posB)+1
			del(blue[0])
			posB = j[1]
			if oran == [] or oran[0]==posO:
				#print "oran attend", oran, posO
				continue
			if oran[0] > posO:
				sig = 1
			else:
				sig = -1
			#print "oran part de", posO
			if abs(dst) > abs(oran[0]-posO):
				posO = oran[0]
			else:
				posO += abs(dst)*sig
			if abs(oran[0]-posO):
				posO += abs(oran[0]-posO)/(oran[0]-posO)
			#print "oran arrice a", posO
		#print "res=", res
	print 'Case #{0}: {1}'.format(i+1, res)
