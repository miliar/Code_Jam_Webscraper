import sys
import math
t = long(sys.stdin.readline())
for i in range(0,t):
	line = sys.stdin.readline().split()
	print 'Case #'+str(i+1)+': ',
	n = long(line[0])
	k = long(line[1])
	x=math.pow(2,n)
	if k%x == x-1:
		print 'ON'
	else:
		print 'OFF'
