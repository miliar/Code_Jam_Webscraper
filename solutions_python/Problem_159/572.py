#!/usr/bin/python
import sys
import math

ifile=sys.argv[1]
lines=open(ifile).read().split("\n")
lines=lines[1:]
case=1

debug=False
#debug=True


def firstmethod(count, mush):
    total=0
    for i in range(1,len(mush)):
        x=int(mush[i-1])
        y=int(mush[i])
        if y < x:
            total+=(x-y)
    return total

def thirdmethod(count, mush):
    minrate=0
    eaten=0
    for i in range(1,len(mush)):
        x=int(mush[i-1])
        y=int(mush[i])
        if y < x:
            rate=x-y
            if minrate < rate:
                minrate=rate

    for i in range(0,len(mush) -1):
        y=int(mush[i])
        if y <= minrate:
            eaten+=y
        else:
            eaten+=minrate

    return eaten


def secondmethod(count, mush):
    first=mush[0]
    last=mush[-1]
    rest=mush[1:-1]
    total=sum(rest)+first-last

    return total

def process(count, mush):
    
    ans1=firstmethod(count, mush)
    #ans2=secondmethod(count, mush)
    ans2=thirdmethod(count, mush)
    return str(ans1)+" "+str(ans2)



while len(lines) != 0:
    if lines[0] == '':
        break
    
    count=int(lines[0])
    mush=lines[1]
    mush=[int(x) for x in mush.split(' ')]
    if debug:
        print("Case #"+str(case)+":")
    output=process(count, mush)
    print("Case #"+str(case)+": "+str(output))
    case+=1
    lines=lines[2:]
	
	
