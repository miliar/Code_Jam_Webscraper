import sys
from decimal import *

filename = sys.argv[1]
f = open(filename, 'r')

numCases = int(f.readline())

for t in range(numCases):
	line = f.readline().strip().split(' ')
	smax = int(line[0])
	people = line[1]
	scount = 0
	friends = 0
	for i in range(smax+1):
		if i == 0:
			scount = int(people[i])
		elif int(people[i]) > 0:
			if scount < i:
				friends = friends + i - scount
				scount = i
			scount = scount + int(people[i])

	print "Case #"+str(t+1)+": "+str(friends)
		
