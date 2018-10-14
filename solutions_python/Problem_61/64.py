#!/usr/bin/python

import sys

def test_group(group):
	pos = {}
	counter = 1
	for i,val in enumerate(group):
		if val:
			pos[i+1] = counter
			counter += 1

	p = len(group) 
	while True:
		if p == 1:
			return True
		if p not in pos:
			return False
		p = pos[p]
d = {}
def handle_case(n):
	if n in d:
		return d[n]
	curr_group = [False] * (n)
	curr_group[n-1] = True
	counter = 0
	while True:
		if test_group(curr_group):
			counter += 1
			counter  = counter % 100003
		for i in xrange(1,n):
			if not curr_group[i]:
				curr_group[i] = True
				break
			else:
				curr_group[i] = False
		else:
			d[n] = counter
			return counter
	
def main(filename):
	fsock = open(filename, "r")
	size = int(fsock.readline())
	for case in range(1,size+1):
		n = int(fsock.readline().rstrip("\n"))
		print "Case #%d: %d" % (case, handle_case(n))
	fsock.close()

if __name__ == "__main__":
	main(sys.argv[1])

