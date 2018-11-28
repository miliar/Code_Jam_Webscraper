#!/usr/bin/python

import os
import sys

fn = sys.argv[1]

fh = open(fn, "r")
T = int(fh.readline().strip())
cases = []
for i in range(T):
    N = map(int, fh.readline().strip().split(" "))[0]
    abs = []
    for j in range(N):
        line = fh.readline().strip().split(" ")
        #print line
        ab = map(int, line)
        abs += [ab]
    L = map(int, fh.readline().strip().split(" "))[0]
    cases += [(N, abs, L)]

fh.close()

#print cases

fh_o = open("out.txt","w")
for i in range(T):
    case = cases[i]
    (N, abs, L) = case
    abs += [[L,0]]
    #print i, case
    reaches = map(lambda x: [], range(N+1))
    #print abs
    reaches[0] = [min(abs[0])]
    for j in range(N):
        #print max([0,reaches[j]])[0]
        try: 
            r1 = filter(lambda x: x > j and abs[x][0] <= max([0,reaches[j]])[0] + abs[j][0], range(N+1))
        except:
            dummy = 1
        #print r1
        for r in r1:
            reaches[r] += [min([abs[r][0] - abs[j][0], abs[r][1] ])]
        #print i, abs, reaches
    if len(reaches[-1]) > 0:
        print >> fh_o, "Case #"+str(i+1)+": YES"
    else:
        print >> fh_o, "Case #"+str(i+1)+": NO"


fh_o.close()
