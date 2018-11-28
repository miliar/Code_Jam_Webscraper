from math import sqrt

with open('A-small-attempt1.in','r') as reading:
	with open('A-small.out','w') as writing:
		no_of_testcase = int(reading.readline())
		for i in range(1, no_of_testcase+1):
			r, t = [int(x) for x in reading.readline().split()]
			s = int((sqrt((2*r - 1)**2 + 8 * t) - (2 * r - 1))/4)
			writing.write('Case #%d: %d\n'%(i,s))
