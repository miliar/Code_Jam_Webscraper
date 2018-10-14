import sys;
import re;
import math;

filename = sys.argv[1]
lines = open(filename, 'r')
lines.readline()

k = 1


for line in lines:
	best = 0
	s = line.split()
	N = int(s[0])
	S = int(s[1])
	p = int(s[2])
	score = [int(x) for x in s[3:N+3]]
	for i in score:
		a = i - p*3
		if a >= -2:
			best = best + 1
		elif a == -4 or a == -3:
			if S > 0 and i >= p:
				best = best + 1
				S = S - 1
		
	print 'Case #'+ str(k)+': ' + str(best)
	k = k+1
