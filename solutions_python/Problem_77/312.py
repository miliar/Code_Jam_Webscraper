#!/usr/bin/env python

import sys
import math

def solve(n, nums):
	#print "START: %s" % (nums)

	numsSorted = sorted(nums)
	numsLeft = []
	for i in range(len(nums)):
		if nums[i] != numsSorted[i]:
			numsLeft.append(nums[i])

	nums = numsLeft
	k = len(nums)
	#print "   Elements unsorted: %s --> %s" % (k, nums)

	hits = 0
	while len(nums) > 0:
		for i in range(2, k+1):
			#print "     Searching %s ordered" % (i)
			numsSorted = sorted(nums)
			#print "        Original: %s" % (nums)
			#print "        Sorted..: %s" % (numsSorted)
			found = False
			removes = 0
			for j in range(0, len(numsSorted)+1-i):
				swapPatern = numsSorted[j:j+i]
				#print "           searching %s on %s" % (swapPatern, nums)
				if swapPatern[0] in nums and swapPatern[0] in nums:
					minIdx = nums.index(swapPatern[0])
					maxIdx = nums.index(swapPatern[0])
					for m in swapPatern:
						curIdx = nums.index(m)
						if curIdx > maxIdx:
							maxIdx = curIdx
						if curIdx < minIdx:
							minIdx = curIdx
					#print "                Range: %s --> %s [j:%s:%s]" % (minIdx, maxIdx, j, j-removes)
					if (maxIdx-minIdx == i-1) and (minIdx == j-removes):
						#print "                Range: %s --> %s" % (minIdx, maxIdx)
						for r in range(i):
							nums.pop(minIdx)
						removes += i
						#hits += math.factorial(i)
						hits += i
						#print "Hits increase to %s" % (hits)
			if len(nums) == 0:
				break

	return float(hits)

def main(infile):
	n = int(infile.readline())
	for i in range(n):
		cmd = infile.readline().split()
		m = int(cmd.pop(0))
		nums = [int(x) for x in infile.readline().split()]
		print 'Case #%s: %.6f' % (i+1, solve(m, nums))

main(sys.stdin)
