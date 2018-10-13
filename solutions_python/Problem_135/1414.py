# -*- coding: iso-8859-1 -*-
from sys import argv
import sys


def removeFour(table, gesucht):
	zeile = [];
	for i in range(1,5):
		if i == gesucht:
			zeile = table.pop()
		else:
			table.pop()
	return [int(i) for i in zeile.split()]



script, filename = argv

txt = open(filename).readlines();

txt.reverse()

cases = int(txt.pop());

#print "number of test: %r" % cases

for case in range(1, cases+1):
	first = int(txt.pop()) # erste antwort
	#interessante zeile finden:
	zeile = removeFour(txt, first)
	#print "erste: %r " % zeile
	
	second = int(txt.pop()) # zweite antwort
	zeile2 = removeFour(txt, second)
	#print "zweite: %r " % zeile2

	result = [x for y in zeile for x in zeile2 if x == y]
	#print result	

	if len(result) == 1:
		print "Case #{0}: {1}".format(case, result[0])
	elif len(result) > 1:
		print "Case #{0}: Bad magician!".format(case)
	else:
		print "Case #{0}: Volunteer cheated!".format(case)


