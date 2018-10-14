import fileinput
from math import sqrt

fi = fileinput.input()
T = int(fi.readline())

for caseN in xrange(T):
	r,t = map(int, fi.readline().strip().split())
	N=0
	while t>=0:
		N+=1
		t-=(2*r+1)
		r+=2
	print 'Case #'+str(caseN+1)+':',N-1
	