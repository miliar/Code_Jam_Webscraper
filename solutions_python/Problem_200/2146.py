#!/usr/bin/python

def ok(nn, i, j):
	for k in xrange(i, j):
		if nn[k] > nn[k+1]:
			return False
	return True

nb = int(raw_input())

for num in xrange(1, nb+1):
	nn = [ int(j) for j in raw_input() ]
	pos = len(nn) -1
	while not ok(nn, 0, pos):
		for j in xrange(pos):
			if nn[j] > nn[j+1]:
				nn[j] -= 1
				for k in xrange(j+1, pos+1):
					nn[k] = 9
				break
		pos = j

	if nn[0] == 0:
		nn.pop(0)
	n = "".join((str(i) for i in nn))
	print "Case #{}: {}".format(num, n)
