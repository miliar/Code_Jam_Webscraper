cases = input()
from itertools import *
from math import *
import bisect
def possiblemults(center,delta):
    bottom = center/1.1
    top = center/0.9
    bottommult = int(ceil(bottom/delta))
    topmult = int(top/delta)
    return (bottommult,topmult)
def find_kit(quants,grreq):
    #import pdb;pdb.set_trace()
    maxkits = 0
    for p,amt in enumerate(quants[0]):
        leftbound,rightbound = possiblemults(amt,grreq[0])
        if leftbound*grreq[0]*0.9>amt or rightbound*grreq[0]*1.1<amt:
            continue
        kitpos = [p]
        for level in range(1,len(quants)):
            leftpos = bisect.bisect_left(quants[level],0.9*grreq[level]*leftbound)
            rightpos = bisect.bisect_right(quants[level],1.1*grreq[level]*rightbound)
            if rightpos<=leftpos:
                break
            kitpos.append(leftpos)
        else:
            #we found a full kit!
            #we can remove it by truncating all lists to just after items
            #except first row which is the one we're iterating on
            maxkits+=1
            #print amt
            for level in range(1,len(quants)):
                #print quants[level][kitpos[level]]
                quants[level] = quants[level][kitpos[level]+1:]
            #import pdb;pdb.set_trace()
    return maxkits
        
for i in range(cases):
    ingr,pkgs = map(int,raw_input().split())
    grreq = map(int,raw_input().split())
    quants = []
    for j in range(ingr):
        quants.append(sorted(map(int,raw_input().split())))
    print "Case #%d: %d"%(i+1,find_kit(quants,grreq))
