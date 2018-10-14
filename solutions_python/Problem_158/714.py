import sys
from decimal import *

filename = sys.argv[1]
f = open(filename, 'r')

numCases = int(f.readline())

for t in range(numCases):
	line = f.readline().strip().split(' ')
	X = int(line[0])
	R = int(line[1])
	C = int(line[2])

	gabriel = False
	if X == 1:
		gabriel = True
	elif X == 2:
		if (R*C)%2 == 0:
			gabriel = True
	elif X == 3:
		if R*C > 3 and (R*C)%3 == 0:
			gabriel = True
	elif X == 4:
		if R*C == 12 or R*C == 16:
			gabriel = True

	if gabriel:
		print "Case #"+str(t+1)+": "+"GABRIEL"
	else:
		print "Case #"+str(t+1)+": "+"RICHARD"