import sys
import numpy as np
import math

infilename = sys.argv[1]
f=open(infilename,'r')
T=int(f.readline())

for t in range(T):
	N=int(f.readline())
	steps = np.array([int(i) for i in f.readline().split()])
	diffs = steps[1:]-steps[:-1]
	y = np.array([0 if i>0 else -1*i for i in diffs]).sum()
	rate = np.zeros(N-1)+np.maximum(-diffs.min(),0)
	z = np.minimum(rate,steps[:-1]).sum()
	print "Case #"+str(t+1)+": "+str(int(y))+" "+str(int(z))

