#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isGood(k_int):
	k = str(k_int)
	for i in range(len(k)-1):
		if int(k[i]) > int(k[i+1]):
			return False
	return True

def solve(k):
	# 1..9 -> k
	# 10 -> 9
	# 11..19 -> k
	# 20,21 -> 19
	# 22..29 -> k
	# 30-32 : 29
	# 33-39 : k

	# 88-89 : k
	# 90-98 : 89
	# 99 : k

	# 100-110


	# if k is "good" : return k
	# else:
		# 次の"good" な数 を a とすると
	
	# 1桁 : 9
	# 2桁 : 19,29,..,99
	# 3桁 : 119,129,..,199, 229,239,299,  339,..399     779, 789, 799  889 999

	# 作り方
	# 	1の位は9
	#   最上位桁は自由
	#   間の桁 : これまでのmax <= x <= 9

	cand = []
	cand.append(9)
	for i in range(10-1):
		cand.append(10*(i+1)+9)

	for i in range(10-1):
		base = 100*(i+1)+9
		for j in range(10-1):
			if i+1<=j+1:
				cand.append(base+10*(j+1))

	cand.reverse()

	if isGood(k):
		return k
	else:
		for e in cand:
			if k>=e:
				return e

if __name__ == "__main__":
	#print solve(3,8,[0,1,2,4,7])
	t = int(raw_input())  # read a line with a single integer
	for i in xrange(1, t + 1):
		k = int(raw_input())
		print "Case #{}: {}".format(i, solve(k))
