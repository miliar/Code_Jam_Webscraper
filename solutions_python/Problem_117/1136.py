#! /usr/bin/env python

import os, sys, inspect
# realpath() with make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)

from collections import defaultdict


def find_possible_cut(lawn, n, m):	# (winner, has_empty)
	N = len(lawn)
	M = len(lawn[0])
	curr_height = lawn[n][m]

	vertically_cut = True
	for i in range(N):
		if(lawn[i][m] > curr_height):
			vertically_cut = False
		
	horizontally_cut = True
	for i in range(M):
		if(lawn[n][i] > curr_height):
			horizontally_cut = False

	return (vertically_cut or horizontally_cut)


def check_possibility(lawn):
	N = len(lawn)
	M = len(lawn[0])

	for i in range(N):
		for j in range(M):
			possible = find_possible_cut(lawn, i, j)
			if not(possible):
				return False

	return True


def main(argv):
	in_file_path = argv[1]
	in_file = open(in_file_path, 'rb')

	out_file_path = '%s.out' % in_file_path
	out_file = open(out_file_path, 'wb')

	T = int(in_file.readline())
	for case_num in range(T):
		params = in_file.readline().split()
		N = int(params[0].strip())
		M = int(params[1].strip())

		lawn = list()
		for i in range(N):
			row_heights = in_file.readline().split()
			row = list()
			for j in range(M):
				height = int(row_heights[j])
				row.append(height)
			lawn.append(row)

		possible = check_possibility(lawn)

		if(possible):
			out_file.write('Case #%d: YES\n' % (case_num+1))
		else:
			out_file.write('Case #%d: NO\n' % (case_num+1))
		

if(__name__ == '__main__'):
	ret = main(sys.argv)
	sys.exit(ret)

