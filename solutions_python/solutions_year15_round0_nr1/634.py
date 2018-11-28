#!/usr/bin/env python
#
# Author: frrp
# Usage: python thisfile.py <input.in >output.out

for case in range(int(raw_input())):
	MAX, audience = raw_input().split()
	MAX = int(MAX)
	total=0
	friends=0
	i=1
	AUD = str(audience)
	for letter in AUD[:-1]:
		total+=int(letter)
		if total+friends < i:
			friends+=1
		i+=1
	print "Case #%d: %s" % (case+1, friends)

