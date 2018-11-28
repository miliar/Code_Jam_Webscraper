#!/usr/bin/env python
import sys

f = open("r01", "rb");
t = int(f.readline());
for i in range(t):
	dd = dict();
	oo = list();
	l = f.readline().split()
	c = int(l.pop(0))
	for j in range(c):
		s = list(l.pop(0))
		dd[(s[0],s[1])] = s[2]
		dd[(s[1],s[0])] = s[2]
	d = int(l.pop(0))
	for j in range(d):
		s = list(l.pop(0))
		oo.append((s[0],s[1]))
	l.pop(0)
	ll = list()
	for x in l[0]:
		ll.append(x)
		while (len(ll)>1 and (ll[-1], ll[-2]) in dd):
			ll = ll[:-2] + [dd[(ll[-1], ll[-2])]]
		clear = lambda tup: (tup[0] in ll and tup[1] in ll)
		if (True in map(clear, oo)):
			ll = list()
	sys.stdout.write("Case #" + str(i+1) + ": [")
	for x in ll[:-1]:
		sys.stdout.write(x+", ")
	if len(ll) > 0: 
		sys.stdout.write( ll[-1])
	print "]"
