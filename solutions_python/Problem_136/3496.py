#!/usr/bin/python

import sys


# 4
# 30.0 1.0 2.0
# 30.0 2.0 100.0
# 30.50000 3.14159 1999.19990
# 500.0 4.0 2000.0

def collect_cookies(c,f,x,rate=2):
	if (x <= c):
		tt = float(x)/rate
		return tt
	else:
		tt = float(c)/rate
		return tt+collect_cookies(c,f,x,rate+2)

def collect_ugly(c,f,x):
	sofar = 0
	i = 0.0
	rate = 2
	while True:
		if (sofar == x):
			return i
		elif (sofar > x):
			return (i-(float(sofar-x)/rate))
		else:
			new_rate = rate+f
			if((float(c)/rate)+(float(x)/new_rate) > (float(x)/rate)):			
				i += float(x)/rate
				sofar = x
			else:
				sofar = 0
				i += float(c)/rate
				rate = new_rate

def input():
	l = sys.stdin.readline()
	(c,f,x) = map(float, l.split(" "))
	return (c,f,x)

if __name__ == "__main__":
	T = int(sys.stdin.readline())
	i = 0
	while(i<T):
		i+=1 
		c,f,x=input()
		tt = collect_ugly(c,f,x)
		print("Case #%d: %0.7f"%(i,tt))