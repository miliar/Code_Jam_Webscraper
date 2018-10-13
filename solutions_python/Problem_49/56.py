import math
C = int(raw_input())
for i in range(0,C):
    N = int(raw_input())
    if N==1:
        x,y,rad = [float(item) for item in raw_input().split(" ")]
        result = rad
    else:
        if N==2:
            x1,y1,rad1 = [float(item) for item in raw_input().split(" ")]
            x2,y2,rad2 = [float(item) for item in raw_input().split(" ")]
            result = max(rad1, rad2)
        else:
            if N==3:
                x1,y1,rad1 = [float(item) for item in raw_input().split(" ")]
                x2,y2,rad2 = [float(item) for item in raw_input().split(" ")]
                x3,y3,rad3 = [float(item) for item in raw_input().split(" ")]            
                d1 = math.sqrt(pow(x1-x2,2) + pow(y1-y2,2)) + rad1+rad2
                d2 = math.sqrt(pow(x1-x3,2) + pow(y1-y3,2)) + rad1+rad3
                d3 = math.sqrt(pow(x2-x3,2) + pow(y2-y3,2)) + rad2+rad3
                mindis = min(d1,d2,d3)
                if mindis==d1:
                    result = max(d1/2, rad3)
                else:
                    if mindis==d2:
                        result = max(d2/2, rad2)
                    else:
                        result = max(d3/2, rad1)
    print "Case #%s: %s" % (i+1, "%.6f"%result)
                    
            
           

