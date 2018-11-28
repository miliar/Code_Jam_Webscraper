#! /usr/bin/env python
import sys
import re
f = open(sys.argv[1])
first = re.split("\s+",f.readline().strip())
L = int(first[0]);
D = int(first[1]);
N = int(first[2]);

dic = []
for i in xrange(D):
    s = f.readline().strip()
    dic.append(s)

for i in xrange(0,N):
    s = f.readline().strip()

    s = s.replace("(","[").replace(")","]")
    pat = re.compile(s)
    
    count = 0
    for d in dic:
        if pat.match(d): count += 1

    print "Case #%d: %d"%(i+1,count)
