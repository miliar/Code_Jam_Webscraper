#!/usr/bin/env python

import re, itertools, sys

def main():
	fname = 'A-large'
	f = open(fname + '.in')
	fout = open(fname + '.out', 'w')
	l, d, n =  map(int, f.readline().rstrip('\n').split(' ') )
	words = [ f.readline().rstrip('\n') for k in xrange( (d) ) ]
	for caseNum in xrange( 1, n+1 ):
		wordMatch = 0
		case = f.readline().rstrip('\n')		
		letters = [ map(None, n) for n in re.findall('(?<=\()[a-z]+(?=\))|[a-z]', case) ]
		
		for word in words:
			flag = 0
			for j in xrange( len(word) ):
				if word[j] in letters[j]:
					flag += 1				
			if flag == l:
				wordMatch += 1
		
		output = 'Case #%d: %s' % (caseNum, wordMatch)
		print output
		fout.write(output + '\n')

	f.close()
	fout.close()

main()

#map(''.join, product(*letters) ):
