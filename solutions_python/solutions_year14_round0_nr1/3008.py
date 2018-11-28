#!/bin/python
import os, sys
T = int(raw_input())
p = sys.stdout.write
for c in xrange(1, T + 1):
	p('Case #%d: '  % c)
	a1 = int(raw_input())

	for i in xrange(1, 5):
		t = map(int, raw_input().split())
		if i == a1:
			l1 = t

	a2 = int(raw_input())
	for i in xrange(1, 5):
		t = map(int, raw_input().split())
		if i == a2:
			l2 = t

	l = list(set(l1) & set(l2))
	
	p(('%d' % l[0]) if len(l) == 1 else ('Bad magician!' if len(l) > 1 else 'Volunteer cheated!'))
	p('\n')

