#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import sys

def main():
	filename = sys.argv[1]
	f = open(filename, 'r')
	output = open("result.out", 'w')
	
	nTestCases = int(f.readline())
	
	for x in range(nTestCases):
		line = f.readline()
		shyMax = int(line.split(" ")[0])
		people = [int(c) for c in line.split(" ")[1] if c != "\n"]
		
		peopleStanding = people[0]
		peopleAdded = 0
		
		for i in range(1, len(people)):
			if peopleStanding >= i:
				peopleStanding += people[i]
			else:
				peopleAdded += (i - peopleStanding)
				peopleStanding += people[i] + (i - peopleStanding)
				
		output.write("Case #" + str(x+1) + ": " + str(peopleAdded) + "\n")
	
	f.close()
	output.close()
	
if __name__ == "__main__":
    main()