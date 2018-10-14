#!/usr/bin/env python
import sys
import re
import urllib
import math
import os
import collections
from timeit import Timer

def subset(): 
	lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]

def output(case, answer):
	return "Case #%d: %d\n" % (case, answer)

def pos(a):
	output = []
	i = 0
	while i < len(a):
		output.append(a)
		a = a[1:] + a[0]
		i += 1
	return output

def main(filein, fileout):
	case = 0
	f = open(filein, 'r')
	o = open(fileout, 'w')
	times = int(f.readline())
	while case < times:
		data = [int(val) for val in f.readline().split(" ")]
		lower = data[0]
		upper = data[1]
		checkvals = [str(val+lower) for val in range(upper+1-lower)]
		answer = 0
		used = []
		for s in checkvals:
			found = []
			possible = [int(val) for val in pos(s)]
			for val in possible:
				if val > int(s) and val <= upper and val not in found:
					answer += 1
					found.append(val)
		case += 1
		o.write(output(case, answer))
	f.close()
	o.close()

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[1][:-2]+'out')
