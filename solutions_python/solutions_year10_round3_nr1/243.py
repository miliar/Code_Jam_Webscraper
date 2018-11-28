#!/usr/bin/env python
import sys

def solve(p):
    p.sort()
    res = 0
    #print p
    for i in range(len(p)):
        #for j in range(i+1, len(p)):
        #    if p[i][1]>=p[j][0] or p[i][0]>=p[j][1]:
        #        res += 1
        res += len([ j for j in range(i+1,len(p)) if (p[j][0]>p[i][0] and p[j][1]<p[i][1]) or p[j][0]<p[i][0] and p[j][1]>p[i][1] ])
    return res

##############################################

tmp = []
case = 0
for i,line in enumerate(file(sys.argv[1])):
    line = line.strip()
    if i==0:
        T=int(line)
        continue

    line = map(int,line.split())
    if len(line)==1 and i>1:
        res = solve(tmp)
        case += 1

        print "Case #%d: %d" % (case, res)
        tmp = []
    elif i>1:
        tmp.append(line)

res = solve(tmp)
case += 1

print "Case #%d: %d" % (case, res)
##############################################
