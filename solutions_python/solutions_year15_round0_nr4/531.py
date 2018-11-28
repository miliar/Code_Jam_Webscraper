import pdb

file = open('D-small-attempt3.in', 'r')
n = int(file.readline())
for i in range(n):
	line = file.readline().strip().split(' ')
	X = int(line[0])
	R = int(line[1])
	C = int(line[2])
	if X == 1:
		res = "GABRIEL"
	elif X == 2:
	 	if (R * C) % X != 0 :
			res = "RICHARD"
		else:
			res = "GABRIEL"
	elif X == 3:
		if min(R,C) == 1 or (R * C) % X != 0:
			res = "RICHARD"
		else:
			res = "GABRIEL"
	else:
		if R * C == 12 or R * C == 16:
			res = "GABRIEL"
		else:
			res = "RICHARD"
	print "Case #%s: %s" % (str(i+1), res)
    
