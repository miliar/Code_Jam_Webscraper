#!/usr/bin/env python
# -*- coding: utf-8 -*-




def time(arg):

	C, F, X = (float(x) for x in arg)

	prod = 2
	t = 0

	while True:

		if t + (X-C)/prod > t + X/(prod+F):
			t = t + C/prod
			prod= prod + F		
		else:
			t = t + X/prod
			break
			
	return(t)

def main (dataIn):
	f = open(dataIn,"r")
	g = open("B.out","a")
	T = int(f.readline())
	
	for i in range(1, T+1):
		line = f.readline().rstrip("\n").split(" ")
		ti = time(line)
		g.write("Case #{}: {}\n".format(i,ti))

	f.close()
	g.close()	

if __name__ == '__main__':
	main("B-large.in")

