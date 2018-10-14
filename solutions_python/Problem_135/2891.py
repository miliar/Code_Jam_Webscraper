#!/usr/bin/python
import os
import sys

f = open("a.dat", "r")
ncase = int(f.readline())
for n in range (ncase):
	pos1 = int(f.readline())
	x = 1
	for x in range(1, pos1):
		f.readline()
	a1 = f.readline().strip().split(" ")
	for x in range(pos1, 4):
		f.readline()
	pos2 = int(f.readline())
	x = 1
	for x in range(1, pos2):
		f.readline()
	a2 = f.readline().strip().split(" ")
	for x in range(pos2, 4):
		f.readline()
	s = set(a1).intersection( set(a2) )
	l = len(s)
	if(l == 1):
		print ("Case #%d: %s" % ((n+1) , s.pop()))
	elif(l > 0):
		print ("Case #%d: Bad magician!" % (n+1))
	elif(l == 0):
		print ("Case #%d: Volunteer cheated!" % (n+1))
f.close()
