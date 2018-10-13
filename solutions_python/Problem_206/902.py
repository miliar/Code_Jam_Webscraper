# Run in command line
# E:\python27\python_nopause.bat A.py < "A-test.in" > "A-test-out.txt" 2>&1
# E:\python27\python_nopause.bat A.py < "A-small-attempt0.in" > "A-small-out.txt" 2>&1
# E:\python27\python_nopause.bat A.py < "A-large.in" > "A-large-out.txt" 2>&1

import os
from sys import *
from math import *

T = int(stdin.readline())
for t in xrange(T):
	D, N = map(int, stdin.readline().split())
	time = []
	for n in xrange(N):
		k, s = map(int, stdin.readline().split())
		time.append(float(D-k)/s)
	res = float(D)/max(time)
	print "Case #%s: %.6f" %(t+1, res)