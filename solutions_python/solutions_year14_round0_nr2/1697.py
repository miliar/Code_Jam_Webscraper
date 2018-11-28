# Problem B. Cookie Clicker Alpha
#
# Author: Phuriphat Boontanon
import sys

if not len(sys.argv):
	sys.exit()
	
input = open(sys.argv[1])
n = int(input.readline())
for k in range(1, n+1):
	d = input.readline().split()
	C = float(d[0])
	F = float(d[1])
	X = float(d[2])
	
	min = X/2.0 # no farm
	waste = 0
	add = 2.0
	while add <= X+500000:
		waste += C/add
		add += F
		if min > (X/add + waste):
			min = X/add + waste
	print 'Case #%d: %.7f'%(k, min)
			