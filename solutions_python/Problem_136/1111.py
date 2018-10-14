#import math

sourcepath = '/Users/alistairpalfreyman/Documents/Code Jam/Input/B-large.in.txt'
destpath = '/Users/alistairpalfreyman/Documents/Code Jam/Output/B-large.in.txt'


def solve(C,F,X):
	c= C
	f = 2
	x = X
	
	delay = 0
	
	while X/f > (C/f + X/(f+F)):
		f += F
		delay += 1	

	f = 2
	result = 0
	for i in xrange(delay):
		result += C/f
		f += F
			
	result += X/(2+delay*F)	
	
	return '%.7f' % result
	

fd = open(sourcepath, 'r')
fo = open(destpath, 'w')
T = int(fd.readline())
for i in range(1,T+1):
	(C,F,X) = fd.readline().split(' ')
	
	result = solve(float(C), float(F), float(X))
	print 'Case #' + str(i) + ': ' + result + '\n',
	fo.write('Case #' + str(i) + ': ' + result + '\n')
	
fd.close()
fo.close()


	