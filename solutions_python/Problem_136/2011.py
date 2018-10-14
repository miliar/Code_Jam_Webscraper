#!/usr/bin/python
import sys

def calc(C, F, X):
	if X <= C:
		return X/2.0
	result = 0
	base = 2.0
	while(C*base <= F*(X-C)):
		result += C/base;
		base += F;
	return result + X/base
	

if __name__ == "__main__":
	T = int(sys.stdin.readline())
	for i in range(T):
		line = sys.stdin.readline()
		nums = line.strip().split(' ')
		result = calc(float(nums[0]), float(nums[1]), float(nums[2]))
		print "Case #%d: %.7f" % (i+1, result)