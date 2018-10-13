#!/usr/bin/python

import sys;

ip_f = open(sys.argv[1], 'r');

T = int(ip_f.readline());

for i in range(T):

	ipAsString = ip_f.readline().split();

	S_max = int(ipAsString[0]);
	S_string = ipAsString[1];

	standing = int(S_string[0]);
	deficient = 0;

	for pos in range(S_max):
		toBeAdded = int(S_string[pos+1]);
		if (0 != toBeAdded) and (standing < pos+1):
			deficient = deficient + (pos+1 - standing);
			standing = standing + deficient;
		standing = standing + toBeAdded;

	print("Case #%d: %d" %(i+1, deficient));
