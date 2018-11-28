#!/usr/bin/env python

import sys
import collections

def make_combiner_map(combos):
	m = {}

	for c in combos:
		s1 = c[0:2]
		s2 = s1[::-1]
		m[s1] = c[2]
		m[s2] = c[2]
	
	return m

def make_opposed_map(opposed):
	m = collections.defaultdict(list)

	for o in opposed:
		m[o[0]].append(o[1])
		m[o[1]].append(o[0])

	return m

def solve(c):
	words = c.split()
	
	n_combos = int(words[0])
	combos = []
	opposed = []

	idx = 1
	for i in range(idx, n_combos+1):
		combos.append(words[i])

	idx = n_combos+1
	n_opposers = int(words[idx])
	idx += 1
	for i in range(idx, idx + n_opposers):
		opposed.append(words[i])

	idx = idx + n_opposers
	seq = words[idx+1]

	cmap = make_combiner_map(combos)
	omap = make_opposed_map(opposed)

	cur_seq = []
	cur_opposed = set()

	for i in seq:
		#print 'i', i, 'cur_seq', cur_seq, 'cur_opposed', cur_opposed
		if len(cur_seq) == 0:
			cur_seq.append(i)
			for o1 in omap[i]:
				cur_opposed.add(o1)
		else:
			last2 = ''.join([cur_seq[len(cur_seq)-1], i])
			combined = cmap.get(last2)
			if combined:
				ritem = cur_seq.pop()
				cur_seq.append(combined)
				try:
					cur_seq.index(ritem)
				except ValueError:
					cur_opposed.clear()
					for ei in cur_seq:
						for o1 in omap[ei]:
							cur_opposed.add(o1)
					
				#print "last2 combined to form", combined
			else:
				if i in cur_opposed:
					#print i, "in", cur_opposed
					del cur_seq[:]
					cur_opposed.clear()
				else:
					#print i, "not in", cur_opposed
					cur_seq.append(i)
					for o1 in omap[i]:
						cur_opposed.add(o1)

	return cur_seq

if __name__ == '__main__':
	lines = open(sys.argv[1]).readlines()
	tests = int(lines[0].strip())
	start = 1
	idx = start
	for i in range(start, tests+start):
		tc = lines[i].strip()
		#print tc
		n = solve(tc)
		print 'Case #%d:' % i, n
