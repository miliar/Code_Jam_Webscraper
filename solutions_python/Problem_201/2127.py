import math
from sets import Set
t = input()
for nu in range(0, t):
	case = raw_input()
	case = case.split(" ")
	N = int(case[0])+1
	K = int(case[1])
	log = math.frexp(K)[1]-1
	base = 2 ** log
	gaps = []
	gapVals = Set([])
	for i in range(base, 2 ** (log+1)):
		rem = i - base
		left = rem*N/base
		right = (rem+1)*N/base
		gaps.append([left, right])
		gapVals.add(right-left-1)
	rem = K - base
	maxGap = max(gapVals)
#	print max(gapVals)
#	print gaps
	ls = 0
	lr = 0
	for i in range(0, rem+1):
		flag = 0
		for gap in gaps:
			if (gap[1] - gap[0] -1) == maxGap:
				left = gap[0]
				right = gap[1]
				curr = (left+right)/2
				ls = curr - left -1
				lr = right - curr -1
#				print left, curr, right
				gaps.remove(gap)
				flag = 1
				break
		if flag == 0:
			gap = gaps[0]
			left = gap[0]
			right = gap[1]
			curr = (left+right)/2
			ls = curr - left-1
			lr = right - curr-1
#			print left, curr, right
			gaps.remove(gap)
				
				
#	print gaps
#	left = rem*N/base
#	right = (rem+1)*N/base
#	curr = (left+right)/2
#	ls = curr - left
#	lr = right - curr
#	print left, curr, right
	print "Case #"+`(nu+1)`+": "+`max(ls, lr)`+ " "+ `min(ls,lr)`
