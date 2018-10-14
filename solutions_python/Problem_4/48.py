#!/usr/bin/python


for case in range(input()):
    numE=int(raw_input())
    vTemp1 = raw_input().split(" ")
    vTemp2 = raw_input().split(" ")
    v1=[]
    v2=[]
    vt1=[]
    vt2=[]
    vn = []
    for i in vTemp1:
        v1.append(int(i));
    for i in vTemp2:
        v2.append(int(i));
    v1.sort()
    v2.sort()
    if v1[0] < v2[0] and v1[0]<0:
        for i in v1:
            v2e  = v2[len(v2)-1]
            if v2e == 0:
                vt2.append(0)
            vn.append(i * v2e)  
            v2.pop(v2.index(v2e))
    else:
        v1.reverse()
        for i in v1:
           vn.append(i * v2.pop(0))   

    sum = 0;
    for i in vn:
        sum+=i
    print "Case #%i: %i" % (case+1,sum)
