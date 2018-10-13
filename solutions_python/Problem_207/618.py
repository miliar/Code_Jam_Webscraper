#usr/bin/python
from __future__ import division
import sys
import random

fin = open(sys.argv[1], "r")
fout = open("B.out", "w")

	

T = int(fin.readline())
for ii in xrange(T):
	N, R, O, Y, G, B, V = map(int,fin.readline().split(' '))
	print N
	Y = Y - V
	R = R - G
	B = B - O
	out = []
	if (Y < 0 and V > 0) or (R < 0 and G > 0) or (B < 0 and O > 0):
		out = 'IMPOSSIBLE'
	new_ar = sorted([[R, 'R'], [Y, 'Y'], [B, 'B']], key = lambda x: -x[0])
	print new_ar	
	n1, n2, n3 = new_ar[0][0], new_ar[1][0], new_ar[2][0]
	print n1, n2, n3
	if n1 > (n2 + n3):
		out = 'IMPOSSIBLE'
	else:
		a = (n2 + n3 - n1 + 1)//2
		print a, 'here' 
		count = 0
		n2_new = n2
		n3_new = n3
		for i in range(n1):
			out.append(new_ar[0][1])
			if count < n2 - a: 
				out.append(new_ar[1][1])
				count  = count + 1
				n2_new = n2_new - 1
				#print	
			else:
				out.append(new_ar[2][1])
				n3_new = n3_new - 1
		n2, n3 = n2_new, n3_new	
		print n2, n3	
		if n3 > n2:
			n3, n2 = n2, n3
			new_ar[1][1], new_ar[2][1] = new_ar[2][1], new_ar[1][1]
		while n3 > 0:
			out.append(new_ar[1][1])
			out.append(new_ar[2][1])
			n3 = n3 - 1
			n2 = n2 - 1
		if n2 == 1:
			out.append(new_ar[1][1])
			n2 = n2 -1
		if n2 > 0:
			print 'ERROR'	

	print out.count('R'), out.count('Y'), out.count('B')		
	#print 'first', out		

	if V > 0:
		ind = len (out)
		if 'Y' in out:	
			ind = out.index('Y')
		out1 = out[:ind]  
		for i in range(V):
			out1.append('Y')
			out1.append('V')
		if ind < len(out):
			out = out1[:] + out[ind:]
		else:
			out = out1[:]
	if G > 0:
		ind = len (out)
		if 'R' in out:	
			ind = out.index('R')
		print ind	
		out1 = out[:ind]  
		for i in range(G):
			out1.append('R')
			out1.append('G')
		print out1	
		if ind < len(out):
			out = out1[:] + out[ind:]
		else:
			out = out1[:]	
	if O > 0:
		ind = len (out)
		if 'R' in out:	
			ind = out.index('B')
		out1 = out[:ind]  
		for i in range(O):
			out1.append('B')
			out1.append('O')
		if ind < len(out):
			out = out1[:] + out[ind:]
		else:
			out = out1[:]					



	#if (rest[0] + rest[1]) < n1:
	#	out = 'IMPOSSIBLE'
	#else:	
	
	#print out	
	#fout.write(' '.join(map(str,sol_board_true[i])) + "\n")			
	fout.write("Case #" + str(ii+1) + ": " + ''.join(out) + "\n")