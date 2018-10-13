import math;

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

t=int(input())
for j in range(t):
    mintime=0
    d,n=map(int,input().split())
    for i in range(n):
        k,s=map(int,input().split())
        distLeft=d-k
        time=distLeft/s
        if time>mintime:
            mintime=time
        #print(mintime,time,distLeft)
    time=d/mintime
    stringBeforePointTime,stringInPointTime=map(str,str(time).split('.'))
    stringInPointTime+='0'*10

    print('case #',end='')
    print((j+1),end='')
    print(':',stringBeforePointTime,end='.')
    print(stringInPointTime[0:6])