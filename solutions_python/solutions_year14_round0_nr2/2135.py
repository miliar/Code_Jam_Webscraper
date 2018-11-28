#!/usr/bin/python
with open('input','r') as f:
        data=f.read()
linens = data.splitlines()
linens.reverse()
with open('submit','w') as f:
 for x in range(0,int(linens.pop())):
    items = [float(i) for i in linens.pop().split()]
    C = items[0]
    F = items[1]
    X = items[2]
    rate = 2.0
    timeToGoal = X/rate
    timeToFarm = C/rate
    timeSoFar=0.0
    anticipatedTime=timeSoFar+timeToGoal
    while 1:
        if timeToGoal <= timeToFarm:
                break
        rate+=F
        timeSoFar+=timeToFarm
        timeToFarm = C/rate
        timeToGoal = X/rate
        if timeSoFar+timeToGoal > anticipatedTime:
                break
        else:
                anticipatedTime=timeSoFar+timeToGoal
    thing = "Case #%d: %5.7f\n" % (x+1,anticipatedTime)
    f.write(thing)