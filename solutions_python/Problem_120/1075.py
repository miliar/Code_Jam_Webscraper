#! /usr/bin/env python

import os, sys, inspect
# realpath() with make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)

import math


def count_num_rings(r, t):
	curr_radius = r
	curr_area = 0
	num_rings = 0
	while(True):
		next_area = ((curr_radius+1)**2 - r**2)
		if(curr_area + next_area > t):
			break
		else:
			curr_area += next_area
			curr_radius += 2
			num_rings += 1

	return num_rings

def calc_num_rings(r, t):
	r = float(r)
	t = float(t)

	n = (math.sqrt(4*r**2 - 4*r + 8*t + 1) - 2*r + 1) / 4.0

	return n


def main(argv):
	in_file_path = argv[1]
	in_file = open(in_file_path, 'rb')

	out_file_path = '%s.out' % in_file_path
	out_file = open(out_file_path, 'wb')

	T = int(in_file.readline())
	for case_num in range(T):
		params = in_file.readline().split()
		r = int(params[0].strip())
		t = int(params[1].strip())

		num_rings = count_num_rings(r, t)
		num_rings = calc_num_rings(r, t)
		
		# print 'Case #%d: %f\n' % (case_num+1, num_rings)
		out_file.write('Case #%d: %d\n' % (case_num+1, num_rings))
		

if(__name__ == '__main__'):
	ret = main(sys.argv)
	sys.exit(ret)

