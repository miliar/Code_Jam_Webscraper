import sys
from time import time
f = sys.argv[1]
lines = open(f, 'r').readlines()

for i, line in enumerate(lines):
	if i == 0: continue
	A, B = map(int, line.split(' '))
	
	c = 0
	for j in range(A, B+1):
		js = str(j)
		for p in range(1, len(js)):
			k = int(js[p:] + js[:p])
			if k == j:
				break
			if j < k <= B:
				c += 1
	
	print 'Case #%i: %i' %(i, c)

