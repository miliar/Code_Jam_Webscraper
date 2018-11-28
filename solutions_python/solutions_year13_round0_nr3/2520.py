#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, os


def isFair(line):
	line = line.strip();
	l = len(line)
	former = line[:l/2]
	latter = line[l/2 + (1 if l % 2 else 0):]
	if former == latter:
		return True
	return False

def solve(begin, end):
	import math
	res = 0;
#	print "-----------------------"
#	for i in sq:
#		print ''.join(i)
#	print "-----------------------"
	for num in range(begin, end):
		if isFair(str(num)) and math.sqrt(num).is_integer():
			if isFair(str(int(math.sqrt(num)))):
				print num
				res += 1
	return res
	
def main():
	T = int(sys.stdin.readline())
	for i in range(T):
		inp = sys.stdin.readline();
		nums = [int(n) for n in inp.strip().split()]
		res = solve(nums[0], nums[1]+1)
		print "Case #%d: %s"%(i+1, res)
	

if __name__ == '__main__':
	sys.exit(main())


