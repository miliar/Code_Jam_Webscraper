f = open('test.txt', 'r')

f.readline()
caseN=1
for line in f:
	X,R,C = map(int, line.split())
	Gab=True
	if X > 7:
		Gab = False
	elif X > max(R,C):
		Gab = False
	elif (X + 1) // 2 > min(R,C):
		Gab = False
	elif R*C % X != 0:
		Gab = False
	elif X == 4:
		Gab = min(R,C) > 2
	elif X == 5:
		Gab = max(R,C) != 5 or min(R,C) != 3
	elif X == 6:
		Gab = min(R,C) > 3
	print "Case #%d: %s" % (caseN, "GABRIEL" if Gab else "RICHARD")
	caseN += 1
