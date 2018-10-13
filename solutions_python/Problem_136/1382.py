# -*- coding: iso-8859-1 -*-
from sys import argv
import sys


def readInput(table, gesucht):
	return [int(i) for i in zeile.split()]



script, filename = argv

txt = open(filename).readlines();

txt.reverse()

cases = int(txt.pop());

#print "number of test: %r" % cases

for case in range(1, cases+1):
	line = [float(i) for i in txt.pop().split()] 

	c = line[0]
	f = line[1]
	x = line[2]	

	base = 0
	lttw = x / 2
	ttw = c/2 + x/(c+f) 	
	i = 1	
	while True :
		base += c/(2+f*(i-1))
		ttw = base + x/(2+i*f)
		i += 1
		if (lttw <= ttw):
			break
		else:
			lttw = ttw

	print "Case #{0}: {1}".format(case, lttw)

	if case ==200:
		sys.exit("")
