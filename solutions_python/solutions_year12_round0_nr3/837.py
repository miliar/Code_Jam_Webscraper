#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#	CodeJam 2012: Qualification Round
#	Author: Mahmoud Aladdin (Platter)
#

file_in = open("C.in", 'r')
file_out = open("C.out", "w")

# ======================================
filereadLine = lambda: file_in.readline().strip()
filereadInt = lambda: int(file_in.readline().strip())
filereadInts = lambda: map(int, file_in.readline().strip().split(' '))
# ======================================
import math
# ======================================
res = []

def CntRecycling(a, max_):
	global res
	A = str(a)
	for i in xrange(len(A) - 1):
		str_ = (A[-(i+1):] + A[:-(i+1)])
		new_ = int(str_)
		if  new_ <= max_ and new_ > a:
			if not (a, str_) in res:
				res.append((a, str_))
	
def main():
	global res
	T = filereadInt()
	for t in xrange(1, T + 1):
		print t
		(A, B) = filereadInts()
		res = []
		for n in xrange(A, B + 1):
			CntRecycling(n, B)
		file_out.write("Case #{}: {}\n".format(t, len(res)))
	return 0
if __name__ == '__main__':
	main()
