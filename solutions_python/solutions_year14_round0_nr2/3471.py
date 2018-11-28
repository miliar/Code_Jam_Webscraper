import sys

infile = sys.stdin

def timeToGoal(FarmCount,FarmProduction,CostForFarm,Goal):
    production = 2.0
    time = 0.0
    for farm in range(FarmCount):
        time += CostForFarm/production
        production += FarmProduction
    time += Goal/production
    return time
    

def minumumTime(CostForFarm,FarmProduction,Goal):
    farmCount = 0
    bestTime = timeToGoal(farmCount,FarmProduction,CostForFarm,Goal)
    done = False
    while not done:
        farmCount = farmCount + 1
        nextTime = timeToGoal(farmCount,FarmProduction,CostForFarm,Goal)
        if(nextTime < bestTime):
            bestTime=nextTime
        else:
            done = True;

    return bestTime

T = int(infile.readline())
for case in xrange(T):
    tokens = infile.readline().split()
    C = float(tokens[0])
    F = float(tokens[1])
    X = float(tokens[2]) 

    result = "%f" % minumumTime(C,F,X)

    #print sequence
    print("Case #%d: %s" % (case+1, result))