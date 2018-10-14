#!/usr/bin/python

import sys

f = open("candy.in","rb")
t = int(f.readline())

for i in range(t):
	n = int(f.readline())
	s = map(int,f.readline().split())
	xor = reduce(lambda a,b:a^b,s)
	sum = reduce(lambda a,b:a+b,s)
	sys.stdout.write("Case #"+str(i+1)+": ")
	if (xor != 0):
		sys.stdout.write("NO\n")
	else:
		sys.stdout.write(str(sum - min(s))+"\n")
