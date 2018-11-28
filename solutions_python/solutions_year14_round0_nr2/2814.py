#!/usr/bin/python
import os
import sys
import numpy as np

f = open("b.dat", "r")
ncase = int(f.readline())
for n in range (ncase):
	dt = np.array(f.readline().strip().split(" ")).astype(float)
	s = 2
	c = dt[0]
	a = dt[1]
	x = dt[2]
	t = 0
	ck = 0

	while(ck < x):
		if(x/s < c/s+(x/(s+a))):
			t += x/s
			break
		t += c/s
		s += a

	print ("Case #%d: %.7f" % ((n+1), t))
f.close()
