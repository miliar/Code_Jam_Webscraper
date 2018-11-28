import sys
import re

counts = sys.stdin.readline().split()
L = int(counts[0])
D = int(counts[1])
N = int(counts[2])

dictionary = ''
for k in xrange(D):
	dictionary += sys.stdin.readline() + '#'

for k in xrange(N):
	pattern = sys.stdin.readline().replace('(', '[').replace(')', ']') + '#'
	print 'Case #%d: %d' % (k + 1, len(re.findall(pattern, dictionary)))

