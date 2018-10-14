#!/usr/bin/pythonw
t = int(raw_input())
for c in xrange(1, t + 1):
	s, k =  map(str,raw_input().split())
	n, k = len(s), int(k)
	s = list(s)
	count = 0
	for i in range(n - k + 1):
	    if s[i] == "-":
	        count += 1
	        for j in range(k):
	            s[i + j] = "-" if s[i + j] == "+" else "+"
	if "-" in s:
		print "Case #%d: IMPOSSIBLE" % (c)
	else:
		print "Case #%d: %d" %(c,count)