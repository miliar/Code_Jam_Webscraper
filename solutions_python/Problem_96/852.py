#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#	CodeJam 2012: Qualification Round
#	Author: Mahmoud Aladdin (Platter)
#
file_in = open("B.in", 'r')
file_out = open("B.out", "w")

# ======================================
filereadLine = lambda: file_in.readline().strip()
filereadInt = lambda: int(file_in.readline().strip())
filereadInts = lambda: map(int, file_in.readline().strip().split(' '))
# ======================================
import math
# ======================================

P, S = 0, 0
def IsGood(F):
	global S
	g, s = False, False
	for i in xrange(10, P - 1, -1):
		for j in xrange(i , -1, -1):
			for k in xrange(j, -1, -1):
				if i + j + k == F:
					if i - k < 2:
						g, s = True, False
						return True
					if i - k == 2:
						g, s = True, True
	if g and s and S:
		S -= 1
		return True
	return False
	
def main():
	global P, S
	T = filereadInt()
	for tt in xrange(1, T + 1):
		print tt
		ints = filereadInts()
		N = ints[0]
		S, P, t = ints[1], ints[2], ints[3:]
		cnt = 0
		for i in xrange(N):
			if(IsGood(t[i])):
				cnt += 1
		file_out.write("Case #{}: {}\n".format(tt, cnt))
	return 0
	
if __name__ == '__main__':
	main()
