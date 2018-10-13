#!/usr/bin/python

def solve(cstr, ostr, istr):
    cm={}
    for i in range(len(cstr)/3):
        t = cstr[i*3:i*3+3]
        cm[(t[0],t[1])] = t[2]        
        cm[(t[1],t[0])] = t[2]
    os=set()
    for i in range(len(ostr)/2):
        t = ostr[i*2:i*2+2]
        os.add((t[0], t[1]))
        os.add((t[1], t[0]))

    l=[]
    for i in istr:
        l.append(i)
        while(len(l) >= 2):
            p = (l[-1],l[-2])
            if p in cm:
                l.pop()
                l.pop()
                l.append(cm[p])
                continue

            last=l[-1]
            for cand in l[0:-1]:
                if (last,cand) in os:
                    l = []

            break

            
    return l

        
n = int(raw_input())
for i in range(n):
    t = raw_input().split()
    if t[0] != "0":
        cstr=t[1]
        t=t[2:]
    else:
        cstr=""
        t=t[1:]
        
    if t[0] != "0":
        ostr=t[1]
        t=t[2:]
    else:
        ostr=""
        t=t[1:]
    istr=t[1]
    res = solve(cstr, ostr, istr)
    print "Case #%s: [%s]" % (i+1, ", ".join(res))

    
