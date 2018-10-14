#!/usr/bin/env python

import sys

def countSub(outer, inner):
	if len(inner) == 0: return 1
	ret = 0
	for i in range(len(outer)):
		if outer[i] == inner[0]:
			ret = ret + countSub(outer[i:], inner[1:])
	return ret


def parseFile(fname):
	w = 'welcome to code jam'
	lines = open(fname).read().split('\n')
	count = int(lines[0])
	lines = lines[1:]
	for i in range(count):
		val = countSub(lines[i], w)
		print 'Case #%d: %s' % (i+1, ('%04d' % val)[-4:])

if __name__ == '__main__':
	parseFile(sys.argv[1])

