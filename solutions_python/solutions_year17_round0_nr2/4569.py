import os.path
import sys 

def toInt(nums):
	n = 0
	for i in nums:
		n = n * 10 + i
	return n

def check(n):
	n = int(n)
	if n < 10:
		return True;
	prev = n % 10
	n /= 10
	while (n > 0):
		r = n %	10
		if r > prev:
			return False
		prev = r
		n /= 10
	return True

def run(ind, nums, result):
	if ind >= len(nums):
		return toInt(result)
	# print "%d with %d" % (toInt(result[0:ind]), toInt(nums[0:ind]))
	if toInt(result[0:ind]) < toInt(nums[0:ind]):
		start = 9
	else:
		start = nums[ind]
	# print "ind %d, from %d to %d" % (ind, start, result[ind - 1])
	for i in range(start, result[ind - 1] - 1, -1):
		result[ind] = i
		r = run(ind + 1, nums, result)
		if r != False:
			return r
	return False

def run2(nums):
	n = toInt(nums)
	for i in range(n, -1, -1):
		if check(i) == True:
			return i


fIn = open("B-large.in", "r")
fOut = open("tidy_large.out", "w")
T = int(fIn.readline())
for t in range(0, T):
	line = fIn.readline()
	nums = [0] + [int(line[i]) for i in range(0, len(line)-1)]
	result = [0]*len(nums)
	r = run(1, nums, result)
	# r = run2(nums)
	# print "Case #%d: %d\n" % (t + 1, r)
	fOut.write("Case #%d: %d\n" % (t + 1, r))

