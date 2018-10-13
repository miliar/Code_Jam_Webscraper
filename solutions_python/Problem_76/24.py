#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
DEBUG = False
# DEBUG = True

def pd(*str):
	if DEBUG:
		print str

def main():
	lines = []

	with open(sys.argv[1], 'r') as fp:
		lines = fp.readlines()
	nmax = int(lines.pop(0))
	for n in range(nmax):
		gomi = lines.pop(0)
		line = lines.pop(0)
		p_str = loop(line)
		print "Case #%d: %s" % (n+1, p_str)

def loop(line):
	nums = map(int, line.split())
	tmp = 0
	for n in nums:
		tmp = tmp^n
	if tmp!=0:
		return 'NO'

	r_value = sum(nums) - min(nums)
	return '%d' % (r_value)
	

if __name__=='__main__':
	main()
