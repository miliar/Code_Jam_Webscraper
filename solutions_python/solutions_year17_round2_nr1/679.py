#usr/bin/python
from __future__ import division
import sys
import random

fin = open(sys.argv[1], "r")
fout = open("A.out", "w")

def check_validity(board, R, C):
	lets = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'
	

T = int(fin.readline())
for ii in xrange(T):
	D, N = map(int,fin.readline().split(' '))
	inp = []
	for r in range(N):
		new_line = map(int,fin.readline().split(' '))
		inp.append(new_line)
	
	print inp

	v_min = 0
	for i in range(N):
		K, S = inp[i]
		V = (D - K)/S
		#print V
		if V > v_min:
			v_min = V

	out = D/v_min
	#print out

	fout.write("Case #" + str(ii+1) + ": " + str(out) + "\n")	