#!/usr/bin/python

import re

filename = "A-large"
input_filename = filename + ".in"
output_filename = filename + ".out"


def substitute(str):
	str = re.sub('\(','[',str)
	str = re.sub('\)',']',str)
	return str

def main():
	fi = open(input_filename,"r")
	fo = open(output_filename,"w")
	list = fi.readline().split()
	(L,D,N) = (int(list[0]),int(list[1]),int(list[2]))
	Dict = []
	Patterns = []
	for i in range(D):
		Dict.append(fi.readline())
	for i in range(N):
		Patterns.append(substitute(fi.readline()))
	Regexps = []
	for pattern in Patterns:
		Regexps.append(re.compile(pattern))
	
	i = 1
	for regex in Regexps:
		count = 0
		for word in Dict:
			if regex.match(word):
				count += 1
		fo.write("Case #" + str(i) + ": " + str(count) + "\n");
		i += 1

if __name__ == "__main__":
	main()
