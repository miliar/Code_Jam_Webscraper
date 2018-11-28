#!/usr/bin/python
import sys

def iterate(seq):
	in_list = [int(i) for i in seq]
	s, m = 0, 0
	for min_standing in xrange(len(in_list)):
		now_standing = in_list[min_standing]
		s+=now_standing
		if s<=min_standing:
			m+=1
			s+=1
	return m

data = open(sys.argv[1]).read()
lines = data.splitlines()
input_count = int(lines[0])
for lineindex in range(1,input_count+1):
	data = lines[lineindex].split()
	print 'Case #%d: %d' % (lineindex,iterate(data[1]))
