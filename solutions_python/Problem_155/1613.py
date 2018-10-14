#!/usr/bin/python

N=int(raw_input())
for i in xrange(0,N):
    line = raw_input()
    s_max = line.split()[0]
    audience = line.split()[1]
    p_cnt=0
    f_cnt=0
    for s,p in enumerate(audience):
        if(int(s)>p_cnt+f_cnt):
            f_cnt += int(s)-p_cnt-f_cnt
        p_cnt += int(p)
    print("Case #"+repr(i+1)+": "+repr(f_cnt))
