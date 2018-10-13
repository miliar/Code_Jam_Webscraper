#!/usr/bin/python
#-*-coding: utf-8 -*-
# By François Magimel, aka Linkid <cucumania@gmail.com>

def open_fi(fi):
	fin = []
	fi = open(fi)
	line_n = fi.readline()[:-1]
	N = eval(line_n) #int
	#
	for k in range(0, N):
		train_p = []
		line_t = fi.readline()[:-1]
		T = eval(line_t)*0.01 #int
		if T == 0.60:
			T = 1.0
		#print T
		#
		line = fi.readline()[:-1]
		line = line.split()
		A = eval(line[0]) #int
		B = eval(line[1]) #int
		#
		for i in range(0, A+B):
			line = fi.readline()[:-1]
			line = line.split()
			hoa, hob = line[0][:2], line[1][:2]
			mina, minb = line[0][3:], line[1][3:]
			new_line = [hoa+"."+mina, hob+"."+minb]
			if i<A:
				gare="0"
			else:
				gare="1"
			new_line.extend(gare)
			train_p.append(new_line)
		nA, nB = lect(train_p, T)
		fin.append([k+1, nA, nB])
	crea(fin)

def lect(tp, T):
	tp.sort()
	tA, tB = [], []
	numA, numB = 0, 0
	for u in tp:
		if u[2] == "0":
			tA, tB, numA = cpt(tA, tB, numA, u, T)
		else:
			tB, tA, numB = cpt(tB, tA, numB, u, T)
	return numA, numB
	

def cpt(lia, lib, n, ut, T):
	if len(lia) > 0:
		if lia[0] <= eval(ut[0]):
			lia.pop(0)
		else:
			n += 1
	else:
		n += 1
	ev = eval(ut[1]) + T
	if (int(ev+0.40) > ev):
		ev = ev-0.60+1
	lib.append(ev)
	lib.sort()
	return lia, lib, n

def crea(out):
	newfi = open("timetable.out", "w")
	for i in out:
		char = "Case #%d: %d %d" %(i[0], i[1], i[2])
		newfi.write(char)
		if i[0] != len(out):
			newfi.write("\n")
	newfi.close()
			

open_fi("B-small-attempt1.in")
