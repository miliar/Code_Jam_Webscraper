import sys
import math
def process(case,num,block1,block2):
	block1.sort(reverse=True)
	block2.sort(reverse=True)
	count1 = 0
	count2 = 0
	tmp1 = block1[:]
	tmp2 = block2[:]
	while block1:
		if block1[0] > block2[0]:
			count1 += 1
			block1.pop(0)
			block2.pop(-1)
		else:
			block1.pop(0)
			block2.pop(0)
	block1 = tmp1
	block2 = tmp2
	while block1:
		if block1[0] > block2[0]:
			count2 += 1
			block1.pop(findAtLeast(block1,block2[0]))
			block2.pop(0)
		elif block2[0] > block2[0] - block1[-1]:				
			block1.pop(-1)
			block2.pop(0)
	print "Case #%d: %d %d" % (case, count2, count1)
def findAtLeast(block,num):
	for i in range(len(block)) :
		if block[i] < num:
			return max(i-1,0)
	return 0
	
fs = open(sys.argv[1])
n = int(fs.readline())
for i in range(n) :
	num = int(fs.readline())
	block1 = [float(k) for k in fs.readline().split()]
	block2 = [float(k) for k in fs.readline().split()]
	process(i+1,num,block1,block2)
