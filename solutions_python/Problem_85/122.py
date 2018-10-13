#!/usr/pubsw/bin/python
import sys

sys.setrecursionlimit(10000)
#print sys.getrecursionlimit()

def processExample(L,t,dist_list,case_num):
    mintime = recProcess(0,L,t,dist_list)
    printResult(case_num,int(mintime+0.5))

def recProcess(timeSoFar,L,t,remDists):
    # base cases
    if len(remDists) == 0:
       return timeSoFar
    if L == 0:
       return 2*sum(remDists)+timeSoFar
       
    # dist over which we'd get a boost
    usefulDist = 0
    if timeSoFar >= t:
        usefulDist = remDists[0]
    else:
        usefulDist = remDists[0] - (t - timeSoFar)/2
        
    # if a booster would be useless or we don't have one
    if usefulDist <= 0:
       return recProcess(timeSoFar + 2*remDists[0], L, t, remDists[1:])

    timeHere = (remDists[0]-usefulDist)*2 + usefulDist
    timeWithBoost = recProcess(timeSoFar + timeHere,L-1,t,remDists[1:])
    timeWithoutBoost = recProcess(timeSoFar + 2*remDists[0], L, t, remDists[1:])

    return(min(timeWithBoost,timeWithoutBoost))

def printResult(case_num,mintime):
    print("Case #" + str(case_num) + ": " + str(mintime))

f = open(sys.argv[1])
all = f.readlines()

case_num = 1
for line in all[1:]:
    lineargs = line.split(' ')
    L = int(lineargs[0])
    t = int(lineargs[1])
    N = int(lineargs[2])
    C = int(lineargs[3])
    dist_vals = [int(n) for n in lineargs[4:]]
    dists = dist_vals*(int(N/C+1))
    dists = dists[:N]
    #print(dists)
    processExample(L,t,dists,case_num)
    case_num += 1
