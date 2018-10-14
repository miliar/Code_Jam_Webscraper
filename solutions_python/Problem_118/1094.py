import sys
import math
n = int(sys.stdin.readline())
O = []
for line in sys.stdin:
	[A, B] = line.split()
	a = int(A)
	b = int(B)
	c = 0
	x = math.trunc(math.sqrt(a))
	while x * x < a:
		x = x + 1
	while x * x <= b:
		X = str(x)
		if X == X[::-1]:
			y = x * x
			Y = str(y)
			if Y == Y[::-1]:
				c = c + 1
		x = x + 1
	O = O + [ c ]
i = 1
for o in O:
	print "Case #" + str(i) + ": " + str(o)
	i = i + 1
