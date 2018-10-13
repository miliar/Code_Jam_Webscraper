#!/usr/bin/python
import re

f_in = open('A-large.in','r')
f_out = open('A-large.out','w')

ws = f_in.readline().rsplit()

dictionary = []
for c in range(1, int(ws[1])+1 ): dictionary.append(f_in.readline().strip())

case = 1
for line in f_in:
	line = line.replace('(','[').replace(')',']').strip()
	count = 0
	for w in dictionary: count += re.subn(line,'',w)[1]
	f_out.write( 'Case #' + str(case) + ': ' + str(count) + '\n' )
	case+=1
