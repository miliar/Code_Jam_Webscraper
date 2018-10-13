#!/usr/bin/python

import sys

def solve(sequence):
	numbers = []
	colors = []
	blue = []
	orange = []
	for s in sequence:
		if (s=='O' or s == 'B'):
			colors.append(s)
		else:
			numbers.append(int(s))
	assert(len(numbers)==len(colors))
	for i in range(0, len(numbers)):
		if colors[i] == 'O':
			orange.append(numbers[i])
		else:
			blue.append(numbers[i])
	
	t = 0
	posBlue = 1
	posOrange = 1
	currBlue = 0
	currOrange = 0
	pressed = 0
	# print(blue)
	# print(orange)
	# print(colors)
	while pressed < len(colors):
		t += 1
		bluePressed = False
		orangePressed = False
		# check if we can press a button
		if len(blue) > 0 and posBlue == blue[currBlue] and colors[pressed]=='B':
			# blue can press
			pressed += 1
			if currBlue+1 < len(blue):
				currBlue += 1
			bluePressed = True
		elif len(orange) > 0 and posOrange== orange[currOrange] and colors[pressed]=='O':
			# orange can press
			pressed += 1
			if currOrange+1 < len(orange):
				currOrange += 1
			orangePressed = True
		if pressed == len(colors):
			return t

		# movement
		if len(blue) > 0 and posBlue < blue[currBlue] and not bluePressed:
			posBlue += 1
		elif len(blue) > 0 and posBlue > blue[currBlue] and not bluePressed:
			posBlue -= 1
		if len(orange) > 0 and posOrange < orange[currOrange] and not orangePressed:
			posOrange += 1
		elif len(orange) > 0 and posOrange > orange[currOrange] and not orangePressed:
			posOrange -= 1
	return t


f = open(sys.argv[1], "r")
cases = int(f.readline())
for c in range(1, cases+1):
	sequence = f.readline().split()
	print("Case #%d: %d" % (c, solve(sequence[1:])))
