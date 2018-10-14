import sys

def cookiesPerSecond(farms):
    return 2 + (farms * f)

def secondsForFarm(farms):
    return c / cookiesPerSecond(farms)

def timeToWin(farmCount):
    farms = 0
    time = 0
    for i in range(farmCount):
        time += secondsForFarm(farms)
        farms +=1
    return (x / cookiesPerSecond(farms)) + time

def runModel():
    farmCount = 0
    while 1 == 1:        
        farmCount += 1
        if timeToWin(farmCount-1) < timeToWin(farmCount):
            return timeToWin(farmCount-1)

def testRuns(runs):
    global c,f,x,curr_line
    for i in range(0,runs):
        curr_line += 1
        input_line = [float(n) for n in inputs[curr_line].split()]
        c = input_line[0]
        f = input_line[1]
        x = input_line[2]
        print 'Case #'+str(i+1)+':',runModel()

inputs = []
curr_line = 0
c = 0.0
f = 0.0
x = 0.0

with open(sys.argv[1], 'r') as fp:
    inputs = fp.readlines()

runs = int(inputs[curr_line])
testRuns(runs)
