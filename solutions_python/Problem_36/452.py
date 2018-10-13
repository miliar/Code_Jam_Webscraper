#!/usr/bin/python
from __future__ import with_statement
import sys

def solve_problem(input_file):
		
	s = "welcome to code jam"
	i = {}
	for c in s:
		pos = s.find(c, 0)
		if not c in i:
			i[c] = []
			while not pos == -1:
				#print c, pos
				i[c] += [pos]
				pos = s.find(c, pos+1)

	with open(input_file, 'r') as rf:
		count=int(rf.readline())

		#print count	
		for idx in range(0, count):
			#print idx
			line = rf.readline().strip('\n')
			#print line		
			b = [0]*len(s)
			for c in line:
				if c in i:
					#print c, "yes"
					if c == 'w':
						b[0] += 1
					else:
						for o in i[c]:
					#		print o, 
							b[o] += b[o-1]
					#	print 
					#	print b


			print "Case #%d: %04d" % (idx+1, b[len(s)-1]%1000)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		solve_problem(sys.argv[1])
	else:
		print 'enter input file as first paramater'
