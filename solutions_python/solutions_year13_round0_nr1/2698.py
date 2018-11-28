#!/usr/bin/env python
from sys import stdin, stderr
for T in range(1, 1+int(stdin.readline())):
	E=[]
	H=D=U=None
	V=[None for n in range(4)]
	C=stdin.readline()
	#print>>stderr, C
	c=C[0]
	if c=='.':
		E.append((0,0))
		H=D=V[0]=False
	else:
		H=D=V[0]=c
	for n in range(1,4):
		c=C[n]
		if c=='.':
			E.append((0,n))
			H=V[n]=False
		else:
			if H and c!='T' and c!=H: H=False
			V[n]=c
	if H:
		print 'Case #%d:'%T, H, 'won'
		for m in range(4): stdin.readline()
		continue
	U=c
	broken=True
	for m in range(1,3):
		C=stdin.readline()
		c=C[0]
		if c=='.':
			E.append((m,0))
			H=V[0]=False
		else:
			if V[0] and c!='T' and c!=V[0]: V[0]=False
			H=c
		n=1
		while n<4:
			c=C[n]
			if c=='.':
				E.append((m,n))
				H=V[n]=False
				if n-m==0: D=False
				if n+m==3: U=False
			else:
				if H and c!='T' and c!=H: H=False
				if V[n] and c!='T' and c!=V[n]: V[n]=False
				if n-m==0:
					if D and c!='T' and c!=D: D=False
				if n+m==3:
					if U and c!='T' and c!=U: U=False
			n+=1
		if H:
			print 'Case #%d:'%T, H, 'won'
			break
	else: broken=False
	if broken:
		for m in range(4-m): stdin.readline()
		continue
	C=stdin.readline()
	c=C[0]
	if c=='.':
		E.append((3,0))
		H=U=V[0]=False
	else:
		if U and c!='T' and c!=U: U=False
		if U:
			print 'Case #%d:'%T, U, 'won'
			stdin.readline()
			continue
		if V[0] and c!='T' and c!=V[0]: V[0]=False
		if V[0]:
			print 'Case #%d:'%T, V[0], 'won'
			stdin.readline()
			continue
		H=c
	broken=True
	n=1
	while n<4:
		c=C[n]
		if c=='.':
			E.append((3,n))
			H=V[n]=False
		else:
			if V[n] and c!='T' and c!=V[n]: V[n]=False
			if V[n]:
				print 'Case #%d:'%T, V[n], 'won'
				break
			if H and c!='T' and c!=H: H=False
		n+=1
	else: broken=False
	if broken:
		stdin.readline()
		continue
	if H:
		print 'Case #%d:'%T, H, 'won'
		stdin.readline()
		continue
	if D and c!='T' and c!=D: D=False
	if D:
		print 'Case #%d:'%T, D, 'won'
		stdin.readline()
		continue
	if E:
		print 'Case #%d:'%T, 'Game has not completed'
	else:
		print 'Case #%d:'%T, 'Draw'
	stdin.readline()
