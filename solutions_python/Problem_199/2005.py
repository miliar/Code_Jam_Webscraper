#!/usr/bin/python

nb = int(raw_input())

def check(t):
	for i in t:
		if i != "+":
			return False
	return True

for num in xrange(1, nb+1):
	pan, size = raw_input().split()
	pan = [ i for i in pan ]
	size = int(size)

	f=0
	for i in xrange(len(pan) - size+1):
		if pan[i] != "+":
			f += 1
			for j in xrange(size):
				if pan[i+j] == "+":
					pan[i+j] = "-"
				else:
					pan[i+j] = "+"
		if check(pan):
			break
	else:
		f = "IMPOSSIBLE"
			
	print "Case #{}: {}".format(num, f)
