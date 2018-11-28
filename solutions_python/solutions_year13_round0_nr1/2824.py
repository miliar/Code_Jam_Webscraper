#!/usr/bin/python
import string
import operator
def decide(nr_x, nr_o, nr_t, cnt):
	for i in xrange(0, cnt):
		if(nr_x[i] + nr_t[i] == 4):
			return 1
		if(nr_o[i] + nr_t[i] == 4):
			return 2
	return 0;
def solve(l1, l2, l3, l4):
	nelem = 0
	goluri = 0;
	draw = 0
	lnr_x = {0:0,1:0,2:0,3:0}
	lnr_o = {0:0,1:0,2:0,3:0}
	lnr_t = {0:0,1:0,2:0,3:0}
	cnr_x = {0:0,1:0,2:0,3:0}
	cnr_o = {0:0,1:0,2:0,3:0}
	cnr_t = {0:0,1:0,2:0,3:0}
	dnr_x = {0:0,1:0}
	dnr_o = {0:0,1:0}
	dnr_t = {0:0,1:0}
	l = 0;
	for i in xrange(0,4):
#		print i, l, l1[i]
		if l1[i] == 'X':
			lnr_x[l] = lnr_x[l] + 1
			cnr_x[i] = cnr_x[i] + 1
			if i == l:
				dnr_x[0] = dnr_x[0] + 1
			elif i+l == 3:
				dnr_x[1] = dnr_x[1] + 1
		elif l1[i] == 'O':
			lnr_o[l] = lnr_o[l] + 1
			cnr_o[i] = cnr_o[i] + 1
			if i == l:
				dnr_o[0] = dnr_o[0] + 1
			elif i + l == 3:
				dnr_o[1] = dnr_o[1] + 1
		elif l1[i] == 'T':
			lnr_t[l] = lnr_t[l] + 1
			cnr_t[i] = cnr_t[i] + 1
			if i == l:
				dnr_t[0] = dnr_t[0] + 1
			elif i+l == 3:
				dnr_t[1] = dnr_t[1] + 1
		elif l1[i] == '.':
			goluri = goluri + 1
	
	l = 1;
	for i in xrange(0,4):
#		print i, l, l2[i]
		if l2[i] == 'X':
			lnr_x[l] = lnr_x[l] + 1
			cnr_x[i] = cnr_x[i] + 1
			if i == l:
				dnr_x[0] = dnr_x[0] + 1
			elif i+l == 3:
				dnr_x[1] = dnr_x[1] + 1
		elif l2[i] == 'O':
			lnr_o[l] = lnr_o[l] + 1
			cnr_o[i] = cnr_o[i] + 1
			if i == l:
				dnr_o[0] = dnr_o[0] + 1
			elif i + l == 3:
				dnr_o[1] = dnr_o[1] + 1
		elif l2[i] == 'T':
			lnr_t[l] = lnr_t[l] + 1
			cnr_t[i] = cnr_t[i] + 1
			if i == l:
				dnr_t[0] = dnr_t[0] + 1
			elif i+l == 3:
				dnr_t[1] = dnr_t[1] + 1
		elif l2[i] == '.':
			goluri = goluri + 1
	l = 2;
	for i in xrange(0,4):
#		print i, l, l3[i]
		if l3[i] == 'X':
			lnr_x[l] = lnr_x[l] + 1
			cnr_x[i] = cnr_x[i] + 1
			if i == l:
				dnr_x[0] = dnr_x[0] + 1
			elif i+l == 3:
				dnr_x[1] = dnr_x[1] + 1
		elif l3[i] == 'O':
			lnr_o[l] = lnr_o[l] + 1
			cnr_o[i] = cnr_o[i] + 1
			if i == l:
				dnr_o[0] = dnr_o[0] + 1
			elif i + l == 3:
				dnr_o[1] = dnr_o[1] + 1
		elif l3[i] == 'T':
			lnr_t[l] = lnr_t[l] + 1
			cnr_t[i] = cnr_t[i] + 1
			if i == l:
				dnr_t[0] = dnr_t[0] + 1
			elif i+l == 3:
				dnr_t[1] = dnr_t[1] + 1
		elif l3[i] == '.':
			goluri = goluri + 1
	l = 3;
	for i in xrange(0,4):
#		print i, l, l4[i]
		if l4[i] == 'X':
			lnr_x[l] = lnr_x[l] + 1
			cnr_x[i] = cnr_x[i] + 1
			if i == l:
				dnr_x[0] = dnr_x[0] + 1
			elif i+l == 4:
				dnr_x[1] = dnr_x[1] + 1
		elif l4[i] == 'O':
			lnr_o[l] = lnr_o[l] + 1
			cnr_o[i] = cnr_o[i] + 1
			if i == l:
				dnr_o[0] = dnr_o[0] + 1
			elif i + l == 3:
				dnr_o[1] = dnr_o[1] + 1
		elif l4[i] == 'T':
			lnr_t[l] = lnr_t[l] + 1
			cnr_t[i] = cnr_t[i] + 1
			if i == l:
				dnr_t[0] = dnr_t[0] + 1
			elif i+l == 3:
				dnr_t[1] = dnr_t[1] + 1
		elif l4[i] == '.':
			goluri = goluri + 1
	rez = decide(lnr_x, lnr_o, lnr_t, 4)
#	print lnr_x, lnr_o, lnr_t
	if  rez == 1:
		return 'X won'
	elif rez == 2:
		return 'O won'
	else:
		rez = decide(cnr_x, cnr_o, cnr_t, 4)
#		print cnr_x, cnr_o, cnr_t
		if rez == 1:
			return 'X won'
		elif rez == 2:
			return 'O won'
		else:
			rez = decide(dnr_x, dnr_o, dnr_t, 2)
#			print dnr_x, dnr_o, dnr_t
			if rez == 1:
				return 'X won'
			elif rez == 2:
				return 'O won'
			elif goluri > 0:
				return  'Game has not completed'
			else:
				return 'Draw'

f = open('A-small-attempt0.in', 'r');
l1 = f.readline();
T = int(l1)
#print l1
for i in xrange(1,T+1):
	l1 = f.readline();
	l2 = f.readline();
	l3 = f.readline();
	l4 = f.readline();
	l5 = f.readline();
	print "Case #"+str(i)+": "+str(solve(l1,l2,l3,l4))
