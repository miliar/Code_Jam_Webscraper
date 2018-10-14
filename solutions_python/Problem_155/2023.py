#! /usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l',
                    action='store_true',
                    default=False,
                    dest='largeFile',
                    help='Use large practice input instead of small one.')

def personNeeded(arg):
	audience = [int(n) for n in arg[1]]
	count, needed = 0, 0
	for shynessLevel in xrange(len(audience)):
		persons = audience[shynessLevel]
		if persons == 0: continue
		if count >= shynessLevel:
			count += persons
		else:
			diff = shynessLevel - count
			needed += diff
			count += persons + diff
	
	return needed

if __name__ == '__main__':
	args = vars(parser.parse_args())
	filename = 'A-small-attempt0.in' if not args['largeFile'] else 'A-large.in'
	try:
		contents = open(filename).read().splitlines()
	except:
		raise

	totalCases = int(contents[0])
	row = 1
	for case in range (1, totalCases+1):
		print 'Case #' + str(case) + ':', personNeeded(contents[case].split());

