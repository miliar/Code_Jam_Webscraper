#!/usr/bin/python

import sys

for tcase in range(input()):
	ln=raw_input().split(' ')
	
	n=int(ln[0])
	k=int(ln[1])

	ON=1	
	for i in range(n):
		if( ((k>>i)%2) != 1):
			ON=0
			break
	
	if ON:
		sys.stdout.write('Case #%d: ON\n'%(tcase+1))
	else:
		sys.stdout.write('Case #%d: OFF\n'%(tcase+1))
	
	
	
	
