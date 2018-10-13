#!/usr/bin/python
def comp(a,b):
    if a[1]==b[1]:
        if a[0][0]=='A':
            return -1
        else:
            return 1
    else:
        return a[1]-b[1]

n=input()
for z in range(n):
    t=input()
    [na, nb]=raw_input().split(' ')
    na=int(na)
    nb=int(nb)

    v=[]
    for i in range(na):
        [start, stop]=raw_input().split(' ')
        [h,m]=start.split(':')
        time = int(h)*60 + int(m)
        v.append(['PA',time])

        [h,m]=stop.split(':')
        time = int(h)*60 + int(m) + t
        v.append(['AB',time])

    for i in range(nb):
        [start, stop]=raw_input().split(' ')
        [h,m]=start.split(':')
        time = int(h)*60 + int(m)
        v.append(['PB',time])

        [h,m]=stop.split(':')
        time = int(h)*60 + int(m) + t
        v.append(['AA',time])

    v.sort(comp)

    print "Case #"+str(z+1)+":",

    c = 0
    t = 0
    for i in range(len(v)):
        if v[i][0]=='PA':
            if t > 0:
                t=t-1
            else:
                c=c+1
        if v[i][0]=='AA':
            t=t+1
    print c,

    c = 0
    t = 0
    for i in range(len(v)):
        if v[i][0]=='PB':
            if t > 0:
                t=t-1
            else:
                c=c+1
        if v[i][0]=='AB':
            t=t+1
    print c

