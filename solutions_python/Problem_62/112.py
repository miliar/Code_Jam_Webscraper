#!/usr/bin/python

import os
import sys

fn = sys.argv[1]

fh = open(fn, "r")
T = int(fh.readline().strip())
cases = []
for i in range(T):
    N = int(fh.readline().strip())
    cases += [{"a":[],"b":[]}]
    for j in range(N):
        line = fh.readline().strip().split(" ")
        #print line[0]
        cases[-1]["a"]+=[int(line[0])]
        cases[-1]["b"]+=[int(line[1])]

fh.close

fh = open("a.out","w")
for (k,case) in enumerate(cases):
    d_e={}
    for i in range(len(case["a"])):
        d_e[case["a"][i]]=case["b"][i]
    bs = []
    for i in sorted(d_e.keys()):
        bs+=[d_e[i]]
    #print bs
    total = 0
    s_bs = set(bs)
    #d_totals={}
    #for i in bs:
    #    d_totals[i]=0
    for b1 in bs[::-1][:-1]:
        total += len(filter(lambda x: x>b1,list(s_bs)))
        s_bs.remove(b1)
    print >> fh, "Case #"+str(k+1)+": "+str(total)

fh.close()
