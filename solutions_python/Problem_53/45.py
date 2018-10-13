#from __future__ import division
import sys

def dbg(obj):
    print>>sys.stderr,obj

f=open('c:\\A-large.in')
case_num=int(f.readline().strip())
for cur_case in range(case_num):
    print 'Case #%d:'%(cur_case+1),
    chainlen,snapcount = [int(s) for s in f.readline().split()]
    c = 2**chainlen
    dbg((chainlen,snapcount,c))
    rest=snapcount%c
    dbg(rest)
    if rest+1==c:
        print 'ON'
    else:
        print 'OFF'
f.close()