#!/usr/bin/env python

import sys, math

#http://snippets.dzone.com/posts/show/753
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]


lines = sys.stdin.readlines()
N = lines.pop(0)
for case_iterator in range(int(N)):
	n = int(lines.pop(0))
	v1 = lines.pop(0).split(" ")
	v2 = lines.pop(0).split(" ")

	for i in range(n):
		v1[i] = int(v1[i])
		v2[i] = int(v2[i])

	prod=0
	for i in range(n):
		prod = prod + v1[i]*v2[i]
	m=prod

	for v in all_perms(v1):
		prod=0
		for i in range(n):
			prod = prod + v[i]*v2[i]
		if prod<m:
			m=prod

	print "Case #"+str(case_iterator+1)+": "+str(m)
