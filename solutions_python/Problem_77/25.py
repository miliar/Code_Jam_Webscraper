#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import copy
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
	initial_order = map(int, line.split())
	sorted_list = initial_order[:]
	sorted_list.sort()
	count = 0
	for i,j in zip(initial_order, sorted_list):
		if i==j: count += 1
	return '%.6f' % (len(initial_order)-count)

def loop_dame(line):
	initial_order = map(int, line.split())

	N = len(initial_order)
	sorted_list = initial_order[:]
	sorted_list.sort()
	mitenai_list = initial_order[:]
	pd("initial_order", initial_order)
	pd("sorted_list", sorted_list)
	pd("mitenai_list", mitenai_list)
	if initial_order == sorted_list:
		return '%.6f' % (0.0,)
	
	loop_count = 0
	while len(mitenai_list)!=0:
		loop_count += 1
		start = mitenai_list.pop(0)
		current = initial_order[sorted_list.index(start)]
		while current!=start:
			mitenai_list.remove(current)
			current = initial_order[sorted_list.index(current)]

	return '%.6f' % (total_time)

if __name__=='__main__':
	main()
