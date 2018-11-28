#coding=utf-8

from itertools import combinations
from bisect import bisect_right

def init():
	ret = ["1","2","3"]
	for i in range(1,50):
		left_len = i / 2
		#10000...
		for j in range(0,3 + 1):
			for com in combinations(range(left_len - 1),j):
				left = "1" + "".join(["1" if x in com else "0" for x in xrange(left_len - 1)])
				right = left[::-1]
				md = "0" * (i % 2)
				point = (j + 1) * 2
				ret.append(left + md + right)
				if i % 2 == 1:
					ret.append(left + "1" + right)
					if point + 4 < 10:
						ret.append(left + "2" + right)
		
		#20000...
		left = "2" + "0" * (left_len - 1)
		right = left[::-1]
		md = "0" * (i % 2)
		ret.append(left + md + right)
		if i % 2 == 1:
			ret.append(left + "1" + right)
	
	ret = list(set([int(i)**2 for i in ret]))
	ret.sort()
	return ret

def solve(all_answer):
	l,r = [int(i) for i in raw_input().split()]
	l -= 1
	ans = bisect_right(all_answer,r) - bisect_right(all_answer,l)
	return ans

def main():
	
	all_answer = init()
	t = int(raw_input())
	for i in xrange(1,t+1):
		print "Case #%d: %s" % (i,solve(all_answer))


main()