import sys
import numpy

def split_u(s):
	group = []
	start = 0
	for i in xrange(0, len(s)-1):
		if s[i] != s[i+1]:
			group.append(s[start:i+1])
			start = i+1
	group.append(s[start:])
	return group

def is_playable(strs):
	max_in = 0
	for i in xrange(len(strs)):
		if len(strs[i]) > len(strs[max_in]):
			max_in = i
	for j in xrange(len(strs[max_in])):
		for i in xrange(len(strs)):
			if j >= len(strs[i]) or strs[i][j][0] != strs[0][j][0]:
				return 0
	return 1

def my_round(n):
	return int(n + 0.5) if n > 0 else int(n - 0.5)

def group_count(group):
	total = sum(map(len, group))
	goal = my_round(total/float(len(group)))
	count = 0
	for st in group:
		count += abs(goal - len(st))
	return count

def count(groups):
	count = 0
	groups = numpy.array(groups)
	for j in xrange(len(groups[0])):
		# a  bb cc
		# aa b  ccc
		count += group_count(groups[:,j])
	return count 

f = open(sys.argv[1])
N = int(f.readline().strip())
for case in xrange(1, N+1):
	n = int(f.readline())
	strs = []
	for s in xrange(n):
		s = f.readline().rstrip()
		strs.append(split_u(s))
	print "Case #%s:" %(case),
	if is_playable(strs) == 0:
		print "Fegla Won"
	else:
		""
		print count(strs)	
		
