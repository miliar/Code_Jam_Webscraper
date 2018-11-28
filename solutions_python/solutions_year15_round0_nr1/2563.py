#!/usr/bin/python
import sys
f=open(sys.argv[1])
nt=int(f.readline())
for i in range(0,nt):
    smax,shyness_str=f.readline().split(" ")
    smax=int(smax)
    shy_count=[]
    for j in range(0,smax+1):
        shy_count.append(int(shyness_str[j]))
    tot_stood_up = 0
    tot_needed = 0
    for j in range(0,smax+1):
        sicount = shy_count[j]
        #print "Tot Stoodup = %d j = %d needed=%d sicount=%d" % (tot_stood_up,j,tot_needed,sicount)
        if sicount == 0:
            continue
        if tot_stood_up < j:
            tot_needed = tot_needed + (j-tot_stood_up)
            tot_stood_up  = tot_stood_up + (j-tot_stood_up)
        tot_stood_up = tot_stood_up + sicount
    print "Case #%d: %d" % (i+1,tot_needed)
        
