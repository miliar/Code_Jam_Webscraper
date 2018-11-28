import math;
import sys;

def  circles(r,t):
	inner = (4 * r * r) - (4 * r) + (8 * t) + 1;
	b = (2*r) - 1;
	return (math.sqrt(inner) - b) / 4;


ip = open(sys.argv[1]);

noTestCases = int(ip.readline())



for i in range(noTestCases):
	tempArr = ip.readline().split(' ');
	r = int(tempArr[0])
	t = int(tempArr[1])
	noCircles = int(math.floor(circles(r,t)))

	print 'Case #' + str(i+1) + ': ' + str(noCircles)