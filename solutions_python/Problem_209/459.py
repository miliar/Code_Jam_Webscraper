from math import pi


def getArea(panstaken):
    summantel = sum(p[1] for p in panstaken)
    if panstaken:
        maxradi = max(panstaken ,key=lambda x:x[0])[0]        
    else:
        maxradi = 0
        
    def add(pa):
        r,m = pa
        return max(maxradi,r)**2*pi+m+summantel
    return add

def result(pans,panstaken,k):
    
    
    for i in range(k):
        pan = max(pans,key = getArea(panstaken))
        panstaken+= [pan]
        pans.remove(pan)    
  
    return getArea(panstaken)((0,0))
    
t = int(input()) 
for i in range(1, t + 1):    
    n,k = [int(p) for p in input().split(" ")]
    pans = []
    for u in range(n):
        pans.append(tuple(int(p) for p in input().split(" ")))
    pans = [(r,r*2*pi*h) for r,h in pans]
    print("Case #{}: {}".format(i, result(pans,[],k)))
