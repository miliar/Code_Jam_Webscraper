import psyco
import sys
import itertools
import re

psyco.full()

test_input = r'''5
2
mmaw
maw
2
gcj
cj
2
maww
maw
2
abc
abc
2
abb
aab'''.split('\n')

DEBUG = False

KNOWN = {

}

def debug(s):
	if not DEBUG:
		return
	sys.stderr.write(str(s) + '\n')

def readline():
	if DEBUG:
		return test_input.pop(0)
	return raw_input()				

def remove_all_dupes(s):
	moves = 0
	for c in s:
		d = c * 2
		while s.count(d) > 1:
			s = s.replace(d, c, 1)
			moves += 1
	return [s, moves]
	
def case(casenum):

	# N strings
	# all strings identical in minimum actions
	# can
		# repeat any character
		# delete one repeated character
		
	# case
		# N - number of strings
		# each a-z string
		
	# output
		# min moves strings identical or
		# "Fegla Won"
	
	
	N = int(readline())
	# debug(["N strings:", N])
	
	strings = []
	for n in xrange(N):
		strings.append(readline())
	
	debug(["strings:", strings])
	
	if len(strings) != 2:
		raise RuntimeError("Can't handle this.")
		
	s1 = strings[0]
	s2 = strings[1]
	
	p = None
	q = None
	
	i = 0
	j = 0
	
	moves = 0
	
	failed = False
	
	while True:
		if i >= len(s1) and j >= len(s2):
			break
	
		# String 1 has ended. String 2 is longer.
		if i >= len(s1):
			for d in s2[j:]:
				if d == q:
					debug("clipping %s" % (d,))
					moves += 1
				else:
					failed = True
					break
			break
			
		# String 2 has ended. String 1 is longer.
		if j >= len(s2):
			for c in s1[i:]:
				if c == p:
					debug("clipping %s" % (c,))
					moves += 1
				else:
					failed = True
					break
			break
	
		c = s1[i]
		d = s2[j]
		
		debug("%s vs %s" % (c, d))
		
		if c != d:
			# Skip duplicates if they don't match.
			if c == p:
				i += 1
				moves += 1
				continue
			elif d == q:
				j += 1
				moves += 1
				continue
			else:
				# Unsolvable.
				failed = True
				break
		
		# Previous values.
		p = c
		q = d
		
		i += 1
		j += 1
	
	if failed:
		output = 'Fegla Won'
	else:
		output = moves
	
	print "Case #%d: %s" % (casenum, output)
	
	

def main():
	numcases = readline()
	for i in xrange(int(numcases)):
		case(i + 1)

main()
