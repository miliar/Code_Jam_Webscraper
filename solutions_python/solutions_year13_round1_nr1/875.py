import sys
from math import sqrt

def P(n, r):
	return 2*r*n + n*(2*n - 1)

def maxBlackRings(r, t):
	n = (-2*r + 1 + sqrt((2*r - 1)**2 + 8*t))/4
	n = int(n)
	usedT = P(n, r)
	while usedT > t:
		n -= 1
		usedT = P(n, r)
	return n

inputFileName = sys.argv[1]

f = file(inputFileName)
fout = file("output.txt", "w")

T = eval(f.readline())

for i in xrange(T):
	r, t = f.readline().split()
	r = eval(r)
	t = eval(t)

	n = maxBlackRings(r, t)

	# Output writing
	fout.write("Case #%d: %d\n" %(i + 1, n))
