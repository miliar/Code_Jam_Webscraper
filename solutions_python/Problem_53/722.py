"""  Problem 1, small input
     George Olive
"""

import re
import sys

infile = open(sys.argv[1],'r')

nlines = int(re.findall(r'\d+',infile.readline())[0])
for i in range(nlines):
	(n,k) = map(int,re.findall(r'\d+',infile.readline()))
	bits=2**n-1
	#print n,k,"->",
	"""for j in range(n-1,-1,-1):
		print k>>j&1,
	print
	print k"""
	print 'Case #'+repr(i+1)+": "+('OFF','ON')[k&bits==bits]


