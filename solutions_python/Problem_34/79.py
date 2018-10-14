#!/usr/bin/env python

import sys
stdin = sys.stdin

L,D,N = map(int , stdin.readline().split())
DD = []
NN = []
for i in range(D):
	DD += [stdin.readline().strip()]

for c in range(N):
	template = []
	tmp = set()
	finish = True
	for x in stdin.readline():
		if x == '(': 
			tmp = set()
			finish = False
		elif x == ')':
			template += [tmp]
			finish = True
		elif x == '\n': 
			break
		elif not finish:
			tmp.add(x)
		else :
			template += [set(x)]
	ans = 0
	for d in DD:
		if sum(map(lambda x,y: x in y, d, template)) == L : 
			ans += 1
	sys.stdout.write('Case #%d: %d\n' % (c+1, ans))
		



