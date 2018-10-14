"""  Problem 2
	 George Olive
"""

import re
import sys

infile = open(sys.argv[1],'r')

nlines = int(re.findall(r'\d+',infile.readline())[0])
for i in range(nlines):
	(runs, seats, ngroups)=	map(int,re.findall(r'\d+',infile.readline()))
	money=0
	#print runs, seats,ngroups
	groups=map(int,re.findall(r'\d+',infile.readline()))
	for run in range(runs):
		#print groups
		s=int(seats)
		onride=[]
		while len(groups) and (groups[0] <= s):
			g=groups.pop(0)
			#print "seated group",g
			onride.append(g)
			s-=g
			money+=g
		#print "start run:", s, "empty seats"
		groups.extend(onride)
	print "Case #"+repr(i+1)+":",money
