import sys
import re

file = open(sys.argv[1], 'r')

fline = file.readline()

p = re.compile('([0-9]*) ([0-9]*) ([0-9]*)')
m = p.search(fline)

Lword = int(m.group(1))
NbrWord = int (m.group(2))
NbrCase =int ( m.group(3))

dico = []
for i in range(0,NbrWord):
	dico.append(file.readline())
	
j = 1
for i in range(0,NbrCase):
	ct = 0
	curCase = file.readline()
	curCase=curCase.replace('(', '[')
	curCase=curCase.replace(')', ']')
	reg = re.compile(curCase)
	for word in dico:
		if reg.match(word) != None:
			ct += 1
	print "Case #" + str(j) + ": " + str(ct)
	j += 1 

	