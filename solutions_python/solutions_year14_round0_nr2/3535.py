import sys
sys.path.append("..")
import codejam as cj
from decimal import *

getcontext().prec=10

cj.name="cookie_clicker"

data=cj.read("_small.txt")

cases=int(cj.getNext(1,data))
#data.insert(1,"1.01663 3.99763 1999.44865")
result=""
result2=""

def getShortestRec(cost,shopAdd,winVal,rate):
    if rate>winVal*(shopAdd/cost):
        return winVal/rate
    time=cost/rate
    #print winVal/rate,winVal,rate    
    return time+min(winVal/rate-time,getShortestRec(cost,shopAdd,winVal,rate+shopAdd))
    
def getShortestDyn(cost,shopAdd,winVal,rate):
    maxRate=rate+shopAdd
    minTime=winVal/rate
    last=minTime
    newMin=minTime
    while maxRate<winVal*(shopAdd/cost):
        straight=winVal/maxRate
        buys=0.0
        tempRate=rate
        while tempRate<maxRate:#in xrange(rate,maxRate+1,shopAdd):
            buys+=cost/tempRate
            tempRate+=shopAdd
            
        oldMin=newMin
        newMin=min(minTime,straight+buys)
        #print minTime
        #print straight+buys
        if newMin>oldMin:
        #if straight+buys>last:
            #print maxRate,shopAdd,"--"
            continue
        last=newMin
        minTime=newMin
        maxRate+=shopAdd
    return minTime

for i in range(0,cases):
    #print i
    result+="Case #"+str(i+1)+": "
    result2+="Case #"+str(i+1)+": "
    temp=cj.getNext(1,data).split(" ")
    
    cost=float(temp[0])
    shopAdd=float(temp[1])
    winVal=float(temp[2])
    temp1=str(getShortestRec(cost,shopAdd,winVal,2.0))
    temp2=str(getShortestDyn(cost,shopAdd,winVal,2.0))
    if temp1!=temp2:
        print "---",temp1,"===",temp2,"...",(i+1),temp
    result+=str(getShortestRec(cost,shopAdd,winVal,2.0))+"\n"
    result2+=str(getShortestDyn(cost,shopAdd,winVal,2.0))+"\n"
    
result=result[0:-1]
#print result
result2=result2[0:-1]
if result==result2:
    cj.finish(result)
    print "success!"
else:
    print "error"