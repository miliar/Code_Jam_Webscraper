#!/usr/bin/python
from string import atoi

cases = input()
for case in range(cases):
    numvals = input()
    vals1 = sorted([atoi(i) for i in raw_input().split(' ')])[::-1]
    vals2 = sorted([atoi(i) for i in raw_input().split(' ')])
    min=0;
    for i in xrange(len(vals1)):
        min+=vals1[i]*vals2[i]
    print "Case #%(case)d: %(min)d" % {'case':case+1, 'min':min}
