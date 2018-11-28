#!/usr/bin/python

def solve(l):
    extra_o=0
    extra_b=0
    cur_o=1
    cur_b=1
    res=0
    for (n,c) in l:
        if c=='O':
            cost = max(0,abs(cur_o-n)-extra_o)
            cost = cost+1            
            res = res+cost
            extra_o = 0
            extra_b = extra_b + cost
            cur_o = n
        else:
            cost = max(0,abs(cur_b-n)-extra_b)
            cost = cost+1            
            res = res+cost
            extra_b = 0
            extra_o = extra_o + cost
            cur_b = n
                
    return res


n = int(raw_input())
for i in range(n):
    t = raw_input().split()
    m = int(t[0])
    l = []
    for j in range(m):
        l.append((int(t[2+2*j]), t[1+2*j]))
    res = solve(l)
    print "Case #%s: %s" % (i+1, res)

