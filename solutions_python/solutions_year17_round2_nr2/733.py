#!/bin/python

def hm(r,y,b):
    if (r>y):
        if (r>b):
            highest=0
            if (y>b):
                middle=1
                lowest=2
            else:
                middle=2
                lowest=1
        else:
            highest=2
            middle=0
            lowest=1
    else:
        if(y>b):
            highest=1
            if(r>b):
                middle=0
                lowest=2
            else:
                middle=2
                lowest=0
        else:
            highest=2
            middle=1
            lowest=0
    return (highest,middle,lowest)

def mapIndex(n):
    if n==0:
        return "R"
    elif n==1:
        return "Y"
    elif n==2:
        return "B"
    else:
        return "FAIL"

caseCount = int(input())
for caseNum in range(1,caseCount+1):

    # case start
    n,r,o,y,g,b,v = [int(n) for n in input().split(" ")]

    # build strings
    #gr = "R"+"GR"*g
    r-=g
    #vy = "Y"+"VY"*v
    y-=v
    #bo = "B"+"OB"*o
    b-=o

    #print(gr)
    #print(vy)
    #print(bo)
    n-=2*(g+v+o)
    #print(n)
    # fail fast
    if(min(r,y,b,n)<0):
        print("Case #{}: IMPOSSIBLE")
        continue

    stack = [r,y,b]
    stall=""
    highest,middle,lowest=hm(r,y,b)

    fCount=stack[highest]-stack[lowest]
    stall+=fCount*(mapIndex(highest)+mapIndex(middle))
    stack[highest]-=fCount
    stack[middle]-=fCount
    # now highest and lowest have same size

    # fail fast
    if(min(stack)<0):
        print("Case #{}: IMPOSSIBLE".format(caseNum))
        continue

    sCount=stack[highest]-stack[middle]
    stall+=sCount*(mapIndex(highest)+mapIndex(lowest))
    stack[highest]-=sCount
    stack[lowest]-=sCount
    # now all have same size

    # fail fast
    if(min(stack)<0):
        print("Case #{}: IMPOSSIBLE".format(caseNum))
        continue

    tCount=stack[highest]
    stall+=tCount*(mapIndex(highest)+mapIndex(middle)+mapIndex(lowest))
    # now all are placed

    # fit in bob strings
    for i in range(g):
        if stall=="":
            stall="RG"
        else:
            stall=stall.replace("R","RGR",1)
    for i in range(v):
        if stall=="":
            stall="YV"
        else:
            stall=stall.replace("Y","YVY",1)
    for i in range(o):
        if stall=="":
            stall="BO"
        else:
            stall=stall.replace("B","BOB",1)

    print("Case #{}: {}".format(caseNum,stall))
    # case end
