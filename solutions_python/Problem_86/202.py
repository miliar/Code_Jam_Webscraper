#!/usr/bin/python
import sys

data = sys.stdin.readlines()
cases = int(data.pop(0))
case = 1

while (case <= cases):
	temp = data.pop(0).split()
	N = int(temp[0]) #num other players
	L = int(temp[1]) #lowest possible note
	H = int(temp[2]) #highest possible note
	temp = data.pop(0).split()
	
	notes = []
	for x in temp:
		notes.append(int(x))
		
	answer = 'NO'
	for test in range(L, H+1):
		y = False
		for note in notes:
			if test % note == 0 or note % test == 0:
				y = True
			else:
				y = False
				break
				
		if y is True:
			answer = test
			break		
	
	sys.stdout.write("Case #%d: %s\n" % (case, str(answer)))
	case += 1