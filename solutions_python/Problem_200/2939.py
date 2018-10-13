import math
t = int(raw_input())
for i in xrange(1, t+1):
	r = raw_input()
	n = int(r)
	pos = 10
	digits = len(r)
	for x in range(digits-1):
		acc_value = n%pos
		next_digit = int(r[digits-2-x])
		this_digit = int(r[digits-1-x])
		if next_digit > this_digit:
			n = n - acc_value - 1
			r = str(n)
		pos = pos * 10
	print "Case #{}: {}".format(i, n)
