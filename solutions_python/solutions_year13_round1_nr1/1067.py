import sys
import math

def f(x, r):
	return (2*x*x) + (2*r-1)*x

T = input()

for test_case in range(T):
	line = raw_input()

	r, t = line.split(' ')
	r = int(r)
	t = int(t)

	circles = 1
	while f(circles+1, r) <= t:
		circles += 1

	print 'Case #' + str(test_case+1) + ': ' + str(circles)