#!/usr/bin/env python3.1
from sys import stdin

lines = stdin.readline().split('\n')
for i in range(int(lines[0])):
	stdin.readline()
	a = [int(x) for x in stdin.readline().strip().split(" ")]
	p = [i+1 != a[i] for i in range(len(a))]
	print("Case #%d: %.6f" % (i+1, sum(p)))
