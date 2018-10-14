lines = open('C-small-attempt0.in').read().split('\n')
T = int(lines[0])
lines= lines[1:]
fout = open('3.out', 'w')

import math
def num_digits(x):
	if x==0 or x==1: return 1
	return int(math.ceil(math.log10(x+1)))

def rotate(x, k=1):
	s = str(x)
	return int(s[k:]+s[:k])

def recycled_x(x, a, b):
	k = num_digits(x)
	s = 0
	for i in xrange(1, k):
		x2 = rotate(x, i)
		if x2>x and x2>=a and x2<=b:
			s+=1
	return s
	
def recycled(a, b):
	s = 0
	for i in xrange(a,b+1):
		#print i, recycled_x(i, a, b)
		s += recycled_x(i, a, b)
	return s
	
	
for t in xrange(1, T+1):
	a, b = [int(x) for x in lines[t-1].split()]
	fout.write("Case #"+str(t)+": "+ str(recycled(a,b))+"\n")