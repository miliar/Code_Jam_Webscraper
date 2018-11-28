#!/usr/bin/env python
import sys
fin=open(sys.argv[1])
cases=int(fin.readline())
for case in range(1,cases+1):
	data=fin.readline().strip().split()
	c=int(data.pop(0))
	subst=dict(map(lambda x:(''.join(sorted(x[:2])),x[2]),data[:c]))
	data=data[c:]
	d=int(data.pop(0))
	opp=dict(map(lambda x:(x[0],x[1]),data[:d])+map(lambda x:(x[1],x[0]),data[:d]))
	data=list(data[-1])
	s=[data.pop(0)]
	while data:
		s.append(data.pop(0))
		if len(s)>1 and ''.join(sorted(s[-2:])) in subst: s=s[:-2]+[subst[''.join(sorted(s[-2:]))]]
		elif s[-1] in opp and opp[s[-1]] in s[:-1]: s=[]
	print "Case #%d: [%s]"%(case,', '.join(s))
