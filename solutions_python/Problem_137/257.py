# REASON NUMBER TWO WHY CIVILIZATIONS DIE:
# MANY SOFTWARE ENGINEERS ARE TRAINED TO
# IMPLEMENT AND SUBMIT SOLUTIONS WITHIN 2.5
# HOURS, BELIEVING THE SOLUTIONS ARE BUG-FREE

import sys
inp = sys.stdin
T = int(inp.readline())

def read_ints():
	return [int(x) for x in raw_input().strip().split()]

def read_floats():
	return [float(x) for x in raw_input().strip().split()]

for t in range(1, T+1):
	R,C,M = read_ints()
	print 'Case #' + str(t) + ':'
	NM = R*C-M
	dotRow = starRow = ''
	for i in range(C):
		dotRow += '.'
		starRow += '*'
	if C==1:
		print 'c'
		for i in range(1,R-M):  print '.'
		for i in range(M):  print '*'
		continue
	if R==1:
		print 'c'+dotRow[1:NM]+starRow[NM:]
		continue
	if M==0:
		print 'c' + dotRow[1:]
		for i in range(1,R): print dotRow
		continue
	if NM==1:
		print 'c' + starRow[1:]
		for i in range(1,R): print starRow
		continue
	if NM<4 or ((R==2 or C==2) and (NM&1)==1) or (R>=3 and C>=3 and (NM==5 or NM==7)):
		print 'Impossible'
		continue
	y=0                        #    z
	for r in range(2,R+1):     #   ...
		c = NM/r               #  .... r    NM = c*r + z  (here c=4, r=2, z=3)
		if c<=1: continue      #  ....
		if c>C: c=C            #    c
		z = NM - c*r
		if z==0 or (R-r>0 and z>=2 and z<=c) or (R-r>1 and z>=4 and z<=2*C and (z-z/2)<=c):
			y=1
			break
	if y==0:
	  for r in range(2,R+1):
		c = NM/r-1
		if c<=1: continue
		if c>C: c=C
		z = NM - c*r
		if z==0 or (R-r>0 and z>=2 and z<=c) or (R-r>1 and z>=4 and z<=2*C and (z-z/2)<=c):
			y=2
			break
	if y>0:
		rows = [starRow]*R
		for i in range(r):
			rows[i] = dotRow[:c] + starRow[c:]
		if R-r>0 and z>=2 and z<=c:
			rows[r] = dotRow[:z] + starRow[z:]
		elif z>=4:
			z2 = z/2
			rows[r]   = dotRow[:z-z2] + starRow[z-z2:]
			rows[r+1] = dotRow[:z2] + starRow[z2:]
		print 'c' + rows[0][1:]
		for i in range(1,R):  print rows[i]
		continue
	else: print 'Impossible'
