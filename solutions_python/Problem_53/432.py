#!/usr/bin/python
from math import pow 
from string import atoi
from math import floor

data = open('input')
data.readline()
out = open('out', 'w')
n=1

for case in data.readlines():
	N, sep, K = case.partition(' ')
	N = atoi(N)
	K = atoi(K)
	Kmask = int((K + 1) % pow(2, N))
	Nmask = N 
	if Kmask | 0:
		out.write("Case #%d: OFF\n"%n)
	else:
		out.write("Case #%d: ON\n"%n)
	n = n+1
