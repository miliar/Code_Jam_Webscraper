#!/usr/bin/env python
import sys
infile = sys.argv[1]
#outfile = sys.argv[2]

indata = open(infile, 'r').readlines()
#print indata

numcases = int(indata[0].strip())
cases = [x.strip().split(' ') for x in indata[1:]]

for j in range(0, numcases):
	case = cases[j]
	numbuttons = int(case[0])
	buttons = []
	for i in range(0, numbuttons):
		buttons.append((case[1+i*2],case[2+i*2]))
	#print buttons
	#Solve case
	orangepos = 1
	orangetime = 0
	bluepos = 1
	bluetime = 0
	for i in range(0, numbuttons):
		neededbutton = int(buttons[i][1])
		if buttons[i][0] == 'O':
			timeneeded = abs(neededbutton-orangepos)
			orangetime = max(orangetime + timeneeded, bluetime) + 1
			orangepos = neededbutton
		elif buttons[i][0] == 'B':
			timeneeded = abs(neededbutton-bluepos)
			bluetime = max(bluetime + timeneeded, orangetime) + 1
			bluepos = neededbutton
	print "Case #" + str(j+1) + ": " + str(max(bluetime, orangetime))
