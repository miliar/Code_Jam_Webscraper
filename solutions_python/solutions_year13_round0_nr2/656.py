#!/usr/bin/env python
import string
from numpy  import *

ipt = open("q2s.i", "r")
opt = open("q2s.o", "w+")

cases = int(ipt.readline())
#print cases

for case in range(cases) :
	case = case+1

	input = ipt.readline().rsplit()
	A = int(input[0])
	B = int(input[1])
#	print A, B

	src = []
	dd = ones((A,B), int) * 100
	dd1 = map(list, zip(*dd))
	dst = map(list, zip(*dd1))
#	print dst

	for rr in range(A) :
		src.append(map(int, ipt.readline().rsplit()))
		print src[rr]

	for rr in range(A) :
		if max(src[rr]) < min(dst[rr]) :
			for kk in range(B) :
				dst[rr][kk] = max(src[rr])
#	print dst 

	src1 = map(list, zip(*src))
	dst1 = map(list, zip(*dst))
#	print src1
#	print dst1

	for rr in range(B) :
		if max(src1[rr]) <= min(dst1[rr]) :
			for kk in range(A) :
				dst1[rr][kk] = max(src1[rr])

#	print src1
#	print dst1
	if src1 == dst1 :
		print("Case #%i: YES" % (case))
		opt.write("Case #%i: YES\n" % (case))
	else :
		print("Case #%i: NO" % (case))
		opt.write("Case #%i: NO\n" % (case))

ipt.close()
opt.close()

