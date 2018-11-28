#!/usr/bin/python
import sys
from pprint import pprint

def main():
	infile = open(sys.argv[1], 'r')
	outfile = open(sys.argv[1][:-2] + 'out', 'w')
	
	for case in xrange(1, int(infile.readline())+1):
		input = infile.readline().split()
		data = input[1:]
		position = [1,1]
		time = [0,0]
		for pointer in xrange(0, int(input[0])):
			index = (data[(pointer*2)]=="B")
			newpos = int(data[(pointer*2)+1])
			
			traveltime = max(position[index], newpos)-min(position[index], newpos)
			position[index] = newpos
			time[index]= max(time[index] + traveltime, time[not index]) + 1
		
		outfile.write("Case #%i: %i\n"%(case, max(time)))
	
	

if __name__ == "__main__":
	main()
