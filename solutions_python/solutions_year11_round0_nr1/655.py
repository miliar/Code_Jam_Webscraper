def main():
    f = open("input.txt",'r')
    lines = f.readlines()
    f.close()
    count = int(lines[0])
    i = 1
    output = ""
    while i<=count:
        stepQueue = []
        steps = lines[i].split(" ")
        nSteps = int(steps[0])
        cN = 1
        while cN<=nSteps:
            cSpot = 1+(cN-1)*2
            stepQueue.append((steps[cSpot], int(steps[cSpot+1])))
            cN+=1
        time = runSim(stepQueue)
        output += "Case #%d: %d\n" %(i,time)
        i+=1
    output = output[:len(output)-1]
    print output
    f = file("output.txt","w")
    f.write(output)
    f.close()

def runSim(queue):
    oQueue = filter(lambda x: x[0]=="O", queue)
    oPos = 1
    bQueue = filter(lambda x: x[0]=="B", queue)
    bPos = 1
    time = 0
    while len(queue)>0:
        nextCMove = queue[0][0]
        if nextCMove == 'O':
            (shouldPress, oPos) = procQueue(queue,oQueue,oPos,True)
            (shouldPress, bPos) = procQueue(queue,bQueue,bPos,shouldPress)
        else:
            (shouldPress, bPos) = procQueue(queue,bQueue,bPos,True)
            (shouldPress, oPos) = procQueue(queue,oQueue,oPos,shouldPress)
        time +=1
    return time

def procQueue(fullQ,myQ,myPos, shouldPress):
    if len(myQ)>0:
        nextPos = myQ[0][1]
        if nextPos!=myPos:
            if nextPos>myPos:
                myPos +=1
            else:
                myPos -=1
        else:
            #Press button if it's time
            if fullQ[0] == myQ[0] and shouldPress:
                myQ.remove(myQ[0])
                fullQ.remove(fullQ[0])
                return (False, myPos)
    return (True, myPos)
                

if __name__=="__main__":
    main()
