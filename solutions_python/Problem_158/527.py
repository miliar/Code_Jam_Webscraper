import sys
import math

tests_count = int(sys.stdin.readline())


for k in xrange(tests_count):
	
	X, R, C = map(int, sys.stdin.readline().split(" "))
	
	status = "RICHARD"

	if X == 1:
		status = "GABRIEL"
	elif X == 2:
		if (R % 2 == 0) or (C % 2 == 0):
			status = "GABRIEL"
		else:
			status = "RICHARD"
	elif X == 3:
		if (R % 3 == 0 and C >= 2) or (R >= 2 and C % 3 == 0):
			status = "GABRIEL"
		else:
			status = "RICHARD"
	elif X == 4:
		if (R % 4 == 0 and C >= 3) or (C % 4 == 0 and R >= 3):
			status = "GABRIEL"
		else: 
			status = "RICHARD"

	print "Case #{}: {}".format(k + 1, status)