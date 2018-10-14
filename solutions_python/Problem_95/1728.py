#!/usr/bin/env
from sys import stdin
import string

intab = string.letters[:26] 
outtab = 'ynficwlbkuomxsevzpdrjgthaq'


outtab = string.letters[:26] 
intab = 'ynficwlbkuomxsevzpdrjgthaq'

print intab
print outtab

trantab = string.maketrans(intab, outtab)




output = open('output1.txt', 'w')
case_no = 1
n = stdin.readlines()

for line in n[1:]:
	line = line.strip()
	line = line.translate(trantab)
	print 'Case #'+str(case_no)+': '+line
	output.write('Case #'+str(case_no)+': '+line+'\n')
	case_no += 1
output.close()
	
	
	


