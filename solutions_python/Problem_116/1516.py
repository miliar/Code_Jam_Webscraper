#/usr/bin/python

import sys

t = int(sys.stdin.readline())

def isxwin(x):
	if ('.' in x):
		return 0
	if not (('X' in x) and ('O' in x)):
		if ('X' in x):
			return 1
		else:
			return 2
	else:
		return 0

for ii in range(t):
	r = ["" for i in range(4)]
	c = ["" for i in range(4)]
	complete = True
	for i in range(4):
		r[i] = sys.stdin.readline().rstrip('\n')
		if ('.' in r[i]):
			complete = False
		for j in range(4):
			c[j]+=r[i][j]
	sys.stdin.readline()
	d1 = ""
	d2 = ""
	for i in range(4):
		d1+=r[i][i]
		d2+=r[i][3-i]

	xwin = False
	owin = False
	for i in range(4):
		x = isxwin(r[i])
		if (x==1):
			xwin = True
		elif (x==2):
			owin = True
		x = isxwin(c[i])
		if (x==1):
			xwin = True
		elif (x==2):
			owin = True
	x = isxwin(d1)
	if (x==1):
		xwin = True
	elif (x==2):
		owin = True
	x = isxwin(d2)
	if (x==1):
		xwin = True
	elif (x==2):
		owin = True

	print "Case #{0:0d}:".format(ii+1),
	if not (xwin or owin):
		if (complete):
			print "Draw"
		else:
			print "Game has not completed"
	else:
		if (xwin):
			print "X won"
		elif (owin):
			print "O won"
