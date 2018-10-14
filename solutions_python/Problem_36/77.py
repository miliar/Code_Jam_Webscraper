#!/usr/bin/env python

import sys

### data structure:
text = "welcome to code jam"

### calculate:
def counter(paragraph, accuracy=0):
    ways = [1]+[0]*len(text)
    for i in paragraph:
        for idx, t in enumerate(text):
            if i == t:
                ways[idx+1] += ways[idx]
		if accuracy > 0: ways[idx+1] %= accuracy
    return ways[-1]

### read loop:

n_lines = int(sys.stdin.readline().strip())
for line in xrange(n_lines):
    para = sys.stdin.readline()
    print "Case #%d: %04d" % (line+1, counter(para, 10000))

