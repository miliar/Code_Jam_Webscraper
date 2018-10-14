

def findTheSpeed(start,speed,d):
    time=-1
    n=len(start)
    for i in range(0,n):
        distance=d-start[i]
        t=distance/speed[i]
        if(t>time):
            time=t
    return d/time


t=int(input())
for i in range(1,t+1):
    temp=input().split()
    d=int(temp[0])
    hs=int(temp[1])
    start=[]
    speed=[]
    for j in range(0,hs):
        temp=input().split()
        start.append(int(temp[0]))
        speed.append(int(temp[1]))
    result=findTheSpeed(start,speed,d)
    temp="{0:.6f}".format(result)
    print("Case #{}: {}".format(i,temp))
