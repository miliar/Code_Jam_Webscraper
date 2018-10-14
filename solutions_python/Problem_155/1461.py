#!/usr/bin/python2
import sys, re

fin = open("A-large.in", "r")
fout = open("A.out", "w")
count = int(fin.readline())

for t in xrange(1, count + 1):
	l = fin.readline().rstrip()
	res = 0
	if l != "0":
		_, arr = l.split()
		s = 0
		
		for i in xrange(len(arr)):
			if arr[i] != "0" and s < i:
				res += i - s
				s = i
			s += ord(arr[i]) - ord("0")
	fout.write("Case #{0}: ".format(t))
	fout.write("{0}\n".format(res))