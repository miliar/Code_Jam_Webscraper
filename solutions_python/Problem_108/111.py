#!/usr/bin/env python
import math
from collections import deque

def process_file(file):
	fsock = open(file)
	text = fsock.read()
	fsock.close()
	lines = text.split('\n')
	return lines

def process_lines(lines):
	ans = []
	i = 0
	T = -1
	
	line = lines[0]
	T = int(line)
	i += 1

	for t in range(T):
		case = {}
		line = lines[i]
		case['N'] = int(line)
		case['d'] = []
		case['l'] = []
		i += 1

		for n in range(case['N']):
			line = lines[i]
			t2 = line.split(' ')
			case['d'].append(int(t2[0]))
			case['l'].append(int(t2[1]))
			i += 1

		line = lines[i]
		case['D'] = int(line)
		i += 1

		ans.append(case)

	return ans

def process_case(line):
	d = line['d']
	l = line['l']
	D = line['D']
	cur = 0
	curD = d[0]
	curL = d[0]
	q = [(0, d[0], d[0])]
	traversed = {}
	if curD + curL >= D:
		return 'YES'
	while len(q) > 0:
		now = q[0]
		q.remove(q[0])
		if traversed.has_key(now[0]) and traversed[now[0]] > now[2]:
			continue
		else:
			traversed[now[0]] = now[2]
		results = getFurthest(now, d, l, D)
		for result in results:
			if result[1] + result[2] >= D:
				return 'YES'
		results.extend(q)
		q = results
		#print '#'
		#print cur
		#print q
		if curD + curL >= D:
			return 'YES'
	return 'NO'

def getFurthest(now, d, l, D):
	cur = now[0]
	curD = now[1]
	curL = now[2]
	# Valid swing is if curD + curL >= nextD AND nextL >= nextD - curD
	maxNextD = curD + curL
	#print maxNextD
	results = []
	for i in range(cur + 1, len(d)):
		'''print '**'
		print curD
		print curL
		print d[i]
		print l[i]'''
		if curD + curL >= d[i]:
			results.append((i, d[i], min(d[i] - curD, l[i])))
		if curD + curL < d[i]:
			break
	return results


if __name__ == "__main__":
	import sys
	filename = sys.argv[1]
	lines = process_file(filename)
	lines = process_lines(lines)
	c = 0
	for line in lines:
		#print line
		#print line['d']
		#print line['l']
		c += 1
		print "Case #%d: %s" % (c, process_case(line))