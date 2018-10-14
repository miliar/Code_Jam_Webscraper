import math

cases = int(input())




def solve(horses,dist):
    best = (dist - horses[0][0])/horses[0][1]
    for i in range(1,len(horses)):
        temp = (dist - horses[i][0])/horses[i][1] 
        if temp > best:
            best = temp
    return dist / best
    

















for i in range(0,cases):
    inflow = str(input()).split(' ')
    dist = int(inflow[0])
    num_horses = int(inflow[1])
    horses=[]
    for j in range(0,num_horses):
        inflow = str(input()).split(' ')
        horses.append([int(inflow[0]),int(inflow[1])])
    print("Case #"+str(i+1)+": "+ str(solve(horses,dist)))



