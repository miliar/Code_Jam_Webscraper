#!/usr/bin/python

import sys


def added_frd(ls):
	if len(ls) > 0:
		#granted = int(ls[0])
		granted = 0
		added = 0
	else:
		return	
	for s in range(len(ls)):
		if s > granted :
			if int(ls[s]) != 0:
				added += s - granted
				granted += s - granted
		granted += int(ls[s])
		#print 'shyness : ', s, 'nb : ', ls[s],'granted : ', granted, 'added : ', added
	return added

#added_frd('10021')

if len(sys.argv) > 1:
	fl = sys.argv[1]
else:
	sys.exit()

with open(fl,'r') as infile:
	T = int(infile.readline())
	with open('output', 'w') as outfile:
		for i in range(T):
			ls = infile.readline().split()[1]
			txt = 'Case #' + str(i+1) + ': ' + str(added_frd(ls)) + '\n'
			outfile.write(txt)

