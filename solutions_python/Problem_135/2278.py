#/usr/bin/python

import sys

t = int(sys.stdin.readline())

for ii in range(t):
	a1 = int(sys.stdin.readline())
	for i in range(4):
		if (i == a1-1):
			x1 = map(int, sys.stdin.readline().split())
		else:
			sys.stdin.readline()
	a2 = int(sys.stdin.readline())
	for i in range(4):
		if (i == a2-1):
			x2 = map(int, sys.stdin.readline().split())
		else:
			sys.stdin.readline()
	count = 0
	for k in x1:
		if k in x2:
			count+=1
			result = k
	print "Case #{0:0d}:".format(ii+1),
	if (count == 0):
		print "Volunteer cheated!"
	elif (count == 1):
		print result
	else:
		print "Bad magician!"