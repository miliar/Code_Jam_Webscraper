import math

def isMin(r, c, x):

	if(max(r,c) < x):
		return False

	m = min(r,c)

	if m >= (x/2) + 1:
		return True
	return False

with open("D-small-attempt0.in") as f:
    lines = f.readlines()

numLines = int(lines[0])

for i in xrange(numLines):
	tmp = lines[i+1].strip().split(' ', 2)
	v = [int(numeric_string) for numeric_string in tmp]

	x = v[0]
	r = v[1]
	c = v[2]

	win = "RICHARD"

	if x == 1:
		win = "GABRIEL"
	elif x == 2:
		if r * c % 2 == 0:
			win = "GABRIEL"
	else:
		m = r * c
		if m % x == 0:
			#if (r >= (x - 1)) and (c >= (x - 1)):
			if isMin(r, c, x) == True:
				win = "GABRIEL"

	print "Case #" + str(i+1) + ": " + win