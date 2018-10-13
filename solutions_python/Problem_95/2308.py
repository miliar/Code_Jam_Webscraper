import enchant
import itertools
from sets import Set
from string import maketrans
		
d = enchant.Dict("en_US")

crypt  = " ynficwlbkuomxsevzpdrjgathaq"
solved = " abcdefghijklmnopqrstuvywxyz"
transTable = maketrans(crypt,solved)

fin = open('c:/A-small-attempt5.in', 'r')
fout = open('c:/output.txt', 'w')

loops = int(float(fin.readline()))
i = 1
while i <= loops:
	crypt = fin.readline()
	testString = crypt.translate(transTable)
	output = 'Case #%d: %s' % (i, testString)
	print output
	fout.write(output)
	i += 1
	
	





