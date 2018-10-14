#!/usr/bin/env python

import sys;

def perms(items,n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in perms(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

N = int(sys.stdin.readline());

for i in xrange(N):
        number = sys.stdin.readline().strip();
	min = int(number)*100;
	test = list(number);
	test.append('0');
	for foo in perms(test,len(test)):
		tmp=int("".join(foo));
		if tmp > int(number) and min > tmp:
			min = int("".join(foo));
	print "Case #%d: %d " % (i+1,min);
		

