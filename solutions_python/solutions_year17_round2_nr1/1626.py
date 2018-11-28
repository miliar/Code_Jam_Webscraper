#!/usr/bin/python3
# author: Jakob Lindqvist
# email:  jakoblindqvist1990@gmail.com


# (g - d) / s = t

import sys
import fileinput

def red(l, D):
	if(len(l)==1): #base case
		return l
	# need to find first intersection
	for i in range(len(l)):
		pass	
	k1 = l[0][0]
	s1 = l[0][1]
	k2 = l[1][0]
	s2 = l[1][1]
	t1 = (D-k1)/s1
	t2 = (D-k2)/s2
	if(t1<t2):
		l.remove((k1,s1))
	else:
		l.remove((k2,s2))
	return l

def solve(l, D, N):
	D = float(D)
	max_speed = 0
	l2 = []
	for i in range(N):
		t = l[i].split()
		kf = float(t[0])
		sf = float(t[1])
		l2.append((kf, sf))
	l2 = sorted(l2, key=lambda tup:tup[0])
	l2 = red(l2, D)
	kr = float(l2[0][0])
	sr = float(l2[0][1])
	tr = (D - kr)/sr
	res = D/tr
	return res

num_test_cases = int(sys.stdin.readline())
for i in range(num_test_cases):
	foo = sys.stdin.readline().rstrip()
	foo = foo.split()
	D = int(foo[0])
	N = int(foo[1])
	horses = []
	for j in range(N):
		horses.append(sys.stdin.readline().rstrip())
	res = solve(horses, D, N)
	res = "{0:.6f}".format(res)
	print("Case #" + str(i+1) + ": " + str(res))

