#!/usr/bin/python

import re
import sys

line = raw_input()
(L, D, N) = line.split(' ', 3)
L, D, N = int(L), int(D), int(N)
words = []
patterns = []
for i in range(0, D):
	line = raw_input()
	words.append(line)
for i in range(0, N):
	line = raw_input()
	patterns.append(line.replace('(', '[').replace(')', ']'))

#print 'words:', ','.join(words)
#print 'patterns:', ','.join(patterns)


X = 1 # licznik petli
for p in patterns:
	K = 0 # ile wyrazow pasuje
	for w in words:
		ret = re.match(p, w)
		if not ret is None:
			K += 1
		
	print 'Case #%d: %d' % (X, K)
	X += 1 # inc
