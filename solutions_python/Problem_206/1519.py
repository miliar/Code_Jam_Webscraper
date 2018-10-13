import random

import sys


def solve(speeds, distances, D):
    n = len(distances)
    times = [0 for i in range(n)]
    for i in range(0,n)[::-1]:
        if i == n-1:
            times[i] = (D-distances[i])/float(speeds[i])
        else:
            time =(D-distances[i])/float(speeds[i])
            if time <= times[i+1]:
                times[i] = times[i+1]
            else:
                times[i] = time
    #print times,speeds,distances,D
    return D/float(times[0])


f = open('a.in', 'r')
g = open('a.out', 'w')

t = int(f.readline())

for i in range(1,t+1):
    
    #read input
    D,N = [int(y) for y in f.readline().split('\n')[0].split(' ')]
    speeds = []
    distances = []
    for j in range(N):
        d,s = [int(y) for y in f.readline().split('\n')[0].split(' ')]
        speeds.append(s)
        distances.append(d)
    print i
    #solve
    ans = solve(speeds,distances,D)
    pr = "Case #"+str(i)+ ": " + str(ans)
    #print pr
    g.write(pr + '\n')


f.close()
g.close()

##for t in range(100):        
##    a = ""
##    for x in range(1000):
##        x = random.randint(0,1)
##        if x == 0:
##            a += "+"
##        else:
##            a += "-"
##
##    s = [x for x in a]
##    k = random.randint(1,1000)
##
##    print solve(s,k,0)
