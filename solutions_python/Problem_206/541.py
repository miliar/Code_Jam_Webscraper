import math
import numpy as np

#fout = open('C:\\Users\\Soheil\\Documents\\Visual Studio 2017\\Projects\\A\\A\\Aoutput-small.out', 'w')
fout = open('C:\\Users\\Soheil\\Documents\\Visual Studio 2017\\Projects\\A\\A\\Aoutput-large.out', 'w')

T=int(input())
for t in range(1,T+1):
    print(t)
    D,N=map(int, input().split())
    horses=[]
    for i in range(0,N):
        horses.append(list(map(int, input().split())))
    horses.sort(reverse=True)
    flag=True
    for h in horses:
        tempEndTime=(D-h[0])/h[1]
        if(flag):
            endTime=tempEndTime
            flag=False
        else:
            if(tempEndTime>endTime):
                endTime=tempEndTime
     
    medVel=D/endTime
    print(horses)
    fout.write("Case #{}: {}\n".format(t,medVel))
fout.close()