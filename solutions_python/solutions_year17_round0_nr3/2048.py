#https://code.google.com/codejam/contest/3264486/dashboard#s=p2
import os
import math

def midFreeStall(stalls):
    distance=0
    for i in range(1,len(stalls)):
        if(stalls[i]-stalls[i-1]>distance):
            distance=stalls[i]-stalls[i-1]
            ret=[stalls[i-1],stalls[i],distance]
    return ret

def loop(items):
    N=int(items[0])
    K=int(items[1])
    stalls=[0,N+1]
    for i in range(K):
        midStall=midFreeStall(stalls)
        min=midStall[0]
        max=midStall[1]
        mid=math.floor(midStall[2]/2+min)
        mindist=mid-min-1   #counts spaces 
        maxdist=max-mid-1   #counts spaces
        stalls.append(mid)
        stalls.sort()
    return [maxdist,mindist]
               
if __name__ == '__main__':
    prob="C-small-1-attempt"                     #filename
    with open(prob+'.out', 'wt') as outfile:
        with open(prob+".in") as infile:
            cases=int(next(infile))
            for case in range(1, cases+1):
                items=next(infile).split()
                out = loop(items)
                casestr="Case #"+str(case)+": "+str(out[0])+" "+str(out[1])+"\n"
                print(casestr)
                outfile.write(casestr)
