import sys
import math

T = int(raw_input())

for c in xrange(1,T+1):
    x=[]
    y=[]
    r=[]
    N = int(raw_input())
    for i in xrange(0,N):        
        arr = [ int(temp) for temp in raw_input().split(' ')]
        x.append(arr[0])
        y.append(arr[1])
        r.append(arr[2])

    if (N==1):
        print "Case #%d: %.8f"%(c,r[0])
    elif (N==2):
        d1 = max(r[0],r[1])
        print "Case #%d: %.8f"%(c,d1)
    elif (N==3):        
        d1 = math.sqrt((x[0]-x[1])*(x[0]-x[1])+(y[0]-y[1])*(y[0]-y[1]))/2
        d1 += 1.0*(r[0]+r[1])/2
                    
        d2 = math.sqrt((x[2]-x[1])*(x[2]-x[1])+(y[2]-y[1])*(y[2]-y[1]))/2
        d2 += 1.0*(r[2]+r[1])/2
                
        d3 = math.sqrt((x[0]-x[2])*(x[0]-x[2])+(y[0]-y[2])*(y[0]-y[2]))/2
        d3 += 1.0*(r[0]+r[2])/2
               
        #print d1,d2,d3
        
        d1 = max(d1,r[2])
        d2 = max(d2,r[0])
        d3 = max(d3,r[1])
        
        print "Case #%d: %.8f"%(c,min(d1,d2,d3))
