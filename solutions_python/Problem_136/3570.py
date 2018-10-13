#!bin/python

import sys

def main(input):

	f = open(input[0],'r')
	f2 = open(input[0][:input[0].index(".")]+".out", 'w')
	lines = []
	for l in f:
		lines += [l]	
	
	numCases = int( lines[0].strip() )

	cases = []
	for i in range(numCases):
		f2.write("Case #" + str(i+1)+ ": ")

		c,f,x = lines[i+1].split()
	
		c = float(c)
		f = float(f)
		x = float(x)

		addCookies = x-c
		
		rate = 2.0
		totalTime = 0.0

		while addCookies/rate > x/(rate+f):
			totalTime += c/rate
			rate += f

		totalTime += x/rate

		f2.write( str(totalTime) + "\n" )	

if __name__ == "__main__":
   main(sys.argv[1:])
