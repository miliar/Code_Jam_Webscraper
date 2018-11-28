#!/usr/bin/python2.7
import re

t = int(raw_input())

si = []
ci = []

for i in range(t):
    li = raw_input()
    li1 = li.split(" ")
    si1 = re.findall('.', li1[1])
    si2 = list(int(i) for i in si1)
    si.append(si2)
    ci.append(0)

for i in range(t):
    sum = si[i][0]
    for j in range(1,len(si[i])):
        if sum < j:
            ci[i] = ci[i] + j - sum
            sum = j
        sum = sum + si[i][j]

for i in range(t):
    print 'Case #%d: %d' %(i+1, ci[i])
    
