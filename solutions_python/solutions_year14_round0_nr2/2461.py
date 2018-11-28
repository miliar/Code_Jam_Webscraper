from __future__ import division
from math import ceil
T = input("")
for x in xrange(T):
	[C, F, X] = [float(i) for i in raw_input("").split()]
	i = max(0, ceil(X/C - 2/F - 1))
	ans = X/(2 + i * F)
	for j in range(int(i)):
		ans += C/(2 + j * F)
	print "Case #" + str(x + 1) + ":", ans