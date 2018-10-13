 #!/usr/bin/python

import sys
import math	
from datetime import datetime

startTime = datetime.now()
sys.setrecursionlimit(20000)

def readn(n):
	return [raw_input() for i in range(n)]
def read():
	return raw_input()
def readints():
	return map(int, read().split())
def wl(n, o):
	print("Case #{0}: {1}".format(n, o))
	
def go():
	(N, D, G) = readints()
	
	if G == 0 and D > 0: return "Broken"
	if G == 100 and D < 100: return "Broken"
	if N >= 100: return "Possible"
	
	for a in range(N+1):
		for b in range(N+1-a):
			if (a!=0 or b!=0) and (100-D)*a==D*b:
				return "Possible"
	return "Broken"	
	
T = int(read())
for TT in range(T):
	wl(TT+1, go())
	
#print(datetime.now()-startTime)