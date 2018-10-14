#!/usr/bin/env python

import sys;

def solve (sli, qli):
	switch = 0;
	qmax = len(qli);
	qidx = 0;
	scnt = len(sli);
	mark = [0 for a in sli];
	cnt = scnt;
	while qidx < qmax:
		while qidx < qmax:
			qry = qli[qidx];
			qidx += 1;
			sidx = sli.index(qry);
			if 0 == mark[sidx]:
				cnt -= 1;
				if 0 == cnt:
					switch += 1;
					mark = [0 for a in sli];
					mark[sidx] = 1; # not free will this time :)
					cnt = scnt - 1;
					break;
				else:
					mark[sidx] = 1;
	return switch;


#sys.stdin = open("sub-3.in");
lines = sys.stdin.readlines();
it = iter(lines);

cmax = int(it.next().rstrip());
cidx = 1;
while cidx <= cmax:
	sno = int(it.next().rstrip());
	sli = [];
	while sno:
		sno -= 1;
		sli.append(it.next().rstrip());
	qno = int(it.next().rstrip());
	qli = [];
	while qno:
		qno -= 1;
		qli.append(it.next().rstrip());
	sw = solve(sli, qli);
	print "Case #%d: %d" % (cidx, sw);
	cidx += 1;
