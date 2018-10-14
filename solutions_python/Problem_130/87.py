from sys import *
from math import pow

f = open(argv[1])
first = True
C = 0
for line in f:
	if first:
		first = False
		continue
	C+=1
	line = line.split()
	N = int(line[0])
	P = int(line[1])
	team = pow(2, N)
	v = team/2
	f1 = team/4
	g = 0
	f2 = 2
	while (v < P and f1 >= 1):
		v += f1
		f1/=2
		g+=f2
		f2*=2
	if (P == team): g = team-1
	v = team
	f1 = team/2
	pos = team-1
	f2 = 1
	while (v > P and v != 1):
		v-=f1
		f1/=2
		pos -= f2
		f2*=2
	print "Case #%d: %d %d"%(C, g, pos)