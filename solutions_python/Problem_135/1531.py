#!/usr/bin/env python
import math
import sys
import os
from os import system

fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for t in range(T):
	a = [[],[]]
	for i in range(2):
		row = int(fp.readline().split()[0])
		for j in range(4):
			l = fp.readline().split()
			if j+1 != row: continue
			for token in l:
				a[i].append(int(token))
	
	ans = [k for k in a[0] if k in a[1]]
	if len(ans) == 1:
		ret = ans[0]
	elif len(ans) == 0:
		ret = "Volunteer cheated!"
	elif len(ans) > 1:
		ret = "Bad magician!"

	fout.write('Case #%d: %s\n'%((t+1),ret))
