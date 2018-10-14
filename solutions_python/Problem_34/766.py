#!/usr/bin/env python

import sys;
import re;

L,D,N = sys.stdin.readline().split();

words="";
for i in xrange(int(D)):
	words = words + sys.stdin.readline();

for i in xrange(int(N)):
	tmp = sys.stdin.readline();
	tmp2 =  re.sub(r'\(','[',tmp);
	pattern = re.sub(r'\)',']',tmp2);

	r = re.compile(pattern);
	l = r.findall(words)

	if l is not None:
		print "Case #%d: %d" % ( i+1,len(l) );

