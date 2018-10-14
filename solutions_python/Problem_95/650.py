#!/usr/bin/env python
import sys
import re
import urllib
import math
import os
from timeit import Timer

#def subset = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]

def output(case, answer):
	return "Case #%d: %s" % (case, answer)

def main(filein, fileout):
	case = 0
	translate = {"a":"y",
		     "b":"h",
		     "c":"e",
		     "d":"s",
		     "e":"o",
		     "f":"c",
		     "g":"v",
		     "h":"x",
		     "i":"d",
		     "j":"u",
		     "k":"i",
		     "l":"g",
		     "m":"l",
		     "n":"b",
		     "o":"k",
		     "p":"r",
		     "q":"z",
		     "r":"t",
		     "s":"n",
		     "t":"w",
		     "u":"j",
		     "v":"p",
		     "w":"f",
		     "x":"m",
		     "y":"a",
		     "z":"q",
		     " ":" ",
		     "\n":"\n",
		     }
	f = open(filein, 'r')
	o = open(fileout, 'w')
	times = int(f.readline())
	while case < times:
		string1 = f.readline()
		temp = ""
		for letter in string1: temp += translate[letter]
		case += 1
		o.write(output(case, temp))
	f.close()
	o.close()

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[1][:-2]+'out')
