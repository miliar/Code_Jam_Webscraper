#!/usr/bin/env python
# Google CodeJam Assignment A

def robotsQualify(steps, script):
     #location and target
    robots = {'B' : [1], 'O' : [1]}
    seconds = 0

    #load targets 
    order = []
    for robot, target in script:
        robots[robot].append(target)
        order.append(robot)

    time = 0
    while order:
        time+=1
        canPress = takeStep(robots)
        if canPress[order[0]]:
            robots[order.pop(0)].pop(0)
    return time




    #for robot, target in script:

def takeStep(robots):
    ret = {'B': False, 'O' :False}
    for robot, move in robots.items():
        if len(move)<2 or move[0] == move[1]: ret[robot] = True
        else: move[0]+=(move[1]>move[0]) and 1 or -1
    return ret


    

def parseInput(line):
    commandList = line.split(' ')
    steps = int(commandList.pop(0))
    ret = []
    while commandList:
        ret.append((commandList.pop(0), int(commandList.pop(0))))
    return {'steps' : steps, 'script' : ret}
    
if __name__ == "__main__":
    mainfn = robotsQualify

    import sys
    if len(sys.argv)==1:
        filename = 'test.in'
    else:
        filename = sys.argv[1]

    f = open(filename)
    line = f.readline()
    for case in range(int(line)):
        args = parseInput(f.readline())
        print "Case #%i: %s" % (case+1, mainfn(**args))
