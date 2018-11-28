import sys
import math
from decimal import *

filename = sys.argv[1]
f = open(filename, 'r')

numCases = int(f.readline())

for t in range(numCases):
	D = int(f.readline())
	P = sorted(map((lambda x: int(x)), f.readline().strip().split(' ')), reverse=True)
	largest = max(P)

	fastest = largest

	for i in range(1, largest):
		time = i
		for j in range(D):
			if(P[j] > i):
				time = int(math.ceil(P[j]/(i*1.0))-1) + time
		if time < fastest:
			fastest = time

	print "Case #"+str(t+1)+": "+str(fastest)

