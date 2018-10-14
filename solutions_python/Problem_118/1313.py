import sys
from array import *
from math import *

def IsPal(x):
	s = str(x)
	s2 = s[::-1]
	return s == s2

in_file = open(sys.argv[1], "r")
out_file = open(sys.argv[1] + ".out", "w")

T = int(in_file.readline())

for i in xrange(T):
	# Parse A and B.
	[A, B] = in_file.readline().split(' ')
	lower_bound = 10 ** long(floor(float(len(A)) / 4.0))
	upper_bound = 10 ** long(ceil(float(len(B)) / 4.0))
	print "lower_bound = " + str(lower_bound)
	print "upper_bound = " + str(upper_bound)
	A = long(A)
	B = long(B)

	# X = []
	count = 0
	#x = rA
	x = lower_bound
	while x <= upper_bound:
		s = str(x)
		st = str(s[::-1])
		
		x1 = long(s + st)
		x1sqr = x1 * x1
		if IsPal(x1sqr) and x1sqr >= A and x1sqr <= B :
			count += 1
			#print x1sqr
			#X.append(x1sqr)

		x2 = long(s + st[1:])
		x2sqr = x2 * x2
		if IsPal(x2sqr) and x2sqr >= A and x2sqr <= B :
			count += 1
			#print x2sqr
			#X.append(x2sqr)

		x += 1

	#X.sort()
	#print X
	out_file.write("Case #" + str(i + 1) + ": " + str(count) + "\n")

in_file.close()
out_file.close()



