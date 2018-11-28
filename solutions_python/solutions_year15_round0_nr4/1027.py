import sys
 
T = int(raw_input())
for t in xrange(1, T + 1):
	x, y, z = map(int, raw_input().split())
	if x == 1:
		print "Case #%d: GABRIEL" % (t)
	if x == 2:
		if ((y * z)% 2 == 0):
			print "Case #%d: GABRIEL" % (t)
		else:
			print "Case #%d: RICHARD" % (t)
 
	if x == 3:
		if ((y * z) % 3 == 0):
			if (y == 1 or z == 1):
				print "Case #%d: RICHARD" % (t)
			else:
				print "Case #%d: GABRIEL" % (t)
		else:
			print "Case #%d: RICHARD" % (t)
	if x == 4:
		if ((y * z) % 4 == 0):
			if (y == 1 or z == 1):
				print "Case #%d: RICHARD" % (t)
			elif (y == 2 or z == 2):
				print "Case #%d: RICHARD" % (t)
			elif (y == 3 or z == 3):
				print "Case #%d: GABRIEL" % (t)
			else:
				print "Case #%d: GABRIEL" % (t)
		else:
			print "Case #%d: RICHARD" % (t)
