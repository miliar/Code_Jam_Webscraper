#!/usr/bin/env python

import sys
import string

rl = sys.stdin.readline
googlerese = string.maketrans('ztcprajkevydiwlbuomqhfgnsx', 'qwertyuiopasdfghjklzxcvbnm')

for nr, x in enumerate(range(int(rl().strip())), start = 1):
	print 'Case #%d: %s' % (nr, rl().strip().translate(googlerese))
