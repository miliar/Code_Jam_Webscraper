#!/usr/bin/python

import sys

f = open("in1.txt","rb")
t = int(f.readline())

rep = "yhesocvxduiglbkrztnwjpfmaq"

for i in range(t):
	st = f.readline()
	st1 = ""
	for j in range(len(st)-1):
		if (st[j]==' '):
			st1+=' '
		else:
			st1+=rep[ord(st[j])-97]
	print "Case #{0:0d}:".format(i+1),st1
