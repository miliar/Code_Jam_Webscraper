#!/usr/bin/python
from permu import permute
from sys import argv
t = (1,2,3,4)
l = []
for i in t:
	for j in t:
		l.append((i,j))
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []
for pos in l:
	a,b = pos
	if a == 1:
		l1.append(pos)
	if a == 2:
		l2.append(pos)
	if a == 3:
		l3.append(pos)
	if a == 4:
		l4.append(pos)
	if b == 1:
		l5.append(pos)
	if b == 2:
		l6.append(pos)
	if b == 3:
		l7.append(pos)
	if b == 4:
		l8.append(pos)
l9 = [(1,1),(2,2),(3,3),(4,4)]
l10 = [(1,4),(2,3),(3,2),(4,1)]
wins = []
wins.append(l1)
wins.append(l2)
wins.append(l3)
wins.append(l4)
wins.append(l5)
wins.append(l6)
wins.append(l7)
wins.append(l8)
wins.append(l9)
wins.append(l10)
flag1 = True
flag2 = False
xo = None
emptind = False
count = -1
casecount = 1
m = []


d = dict()
fin = open(argv[1])
for line in fin:
	if flag1:
		flag1 = False
		continue
	count += 1
	if count == 4:
		count = -1
		for i in range(16):
			d[l[i]] = m[i]
		for lis in wins:
			n = []
			for posit in lis:
				n.append(d[posit])
			xcount = 0
			ocount = 0
			tind = False
			for piece in n:
				if piece == 'X':
					xcount += 1
				if piece == 'O':
					ocount += 1
				if piece == 'T':
					tind = True
				if piece == '.':
					emptind = True
			if tind:
				if xcount == 3:
					xo = True
					flag2 = True
					break
				if ocount == 3:
					xo = False
					flag2 = True
					break
			if xcount == 4:
				xo = True
				flag2 = True
				break
			if ocount == 4:
				xo = False
				flag2 = True
				break
		if flag2:
			if xo:
				result = 'X won'
			else:
				result = 'O won'
		else:
			if emptind:
				result = 'Game has not completed'
			else:
				result = 'Draw'
		flag2 = False
		emptind = False
		print 'Case #' + str(casecount)+':', result	
		m = []
		d = dict()
		casecount += 1
	else:
		m = m + list(line.strip())
