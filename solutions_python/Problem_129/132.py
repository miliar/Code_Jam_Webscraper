def calculateCost( item, N ):
    k = item[1] - item[0]
    #print N,k
    return( N*k - (k-1)*k / 2 )*item[2]



def runOnce( data, N ):
    print "start"
    totalCost= 0
    for item in data:
        totalCost +=calculateCost( item, N )
    data.sort()
##    print data
##    print totalCost
    startOn = []
    for item in data:
        numOn = item[2]
        start = item[0]
        if len(startOn)>0 and startOn[-1][0]==start:
            startOn[-1][1]+= numOn
        else:
            startOn.append([start, numOn])
    for item in data:
        del item[0]
    data.sort()
    endOn = []
    for item in data:
        numOff = item[1]
        end = item[0]
        if len(endOn)>0 and endOn[-1][0]==end:
            endOn[-1][1]+= numOff
        else:
            endOn.append([end, numOff])
##    print "starton", startOn
##    print "endOn" , endOn

    #remove same stations
    onIndex = 0
    offIndex = 0
    while( onIndex < len(startOn) ):
        station = startOn[onIndex][0]
        while endOn[offIndex][0] < station and offIndex < len(endOn):
            offIndex+=1
        if offIndex == len(endOn):
            break
        if station == endOn[offIndex][0]:
            sub = min(startOn[onIndex][1], endOn[offIndex][1])
            startOn[onIndex][1]-= sub
            endOn[offIndex][1] -= sub
        onIndex+=1
    #print "removed duplicates"
    #print startOn, endOn

    newCost = 0
    #print "here"
    backIndex = len(endOn) - 1
    while len(startOn) > 0:
        startStation = startOn[-1][0]

        backIndex = min( len(endOn)-1, backIndex)
        backIndex = max(backIndex, 0)
        while endOn[backIndex][0] > startStation:
            #print backIndex
            backIndex-=1
            if backIndex <0:
                break
        backIndex+=1 #now to 1st smaller station
        numPass = min(startOn[-1][1], endOn[backIndex][1])
        startOn[-1][1] -= numPass
        endOn[backIndex][1] -= numPass
        newCost += calculateCost( [startStation, endOn[backIndex][0], numPass], N)
        if startOn[-1][1] == 0:
            startOn.pop()
        if endOn[backIndex][1] == 0:
            del endOn[backIndex]

        
        
##        startStation = startOn[0][0]
##        endStation = endOn[-1][0]
##        numPeople = min(startOn[0][1], endOn[-1][0])
##        
##        print startOn, endOn, numPeople
##        raw_input()
##        
##        startOn[0][1]-=numPeople
##        endOn[-1][1]-=numPeople
##        if startOn[0][1] == 0:
##            del startOn[0]
##        if endOn[-1][1] == 0:
##            endOn.pop()
    #print "done"
    return totalCost - newCost
           
        



data = [line.strip() for line in open("input.txt")]
output = []
numLines = int(data[0])
lineNum = 1
while(lineNum < len(data)):
    line = [int(token) for token in data[lineNum].split()]
    numStops = line[0]
    numPairs = line[1]
    thisData = []
    for i in range(numPairs):
        temp = [int(token) for token in data[lineNum + i + 1].split()]
        thisData.append(temp)
    output.append(runOnce( thisData, numStops ) )
    lineNum +=numPairs + 1

f = open("output.txt", 'w')
for i in range(len(output)):
    f.write("Case #"+str(i+1)+": "+str(output[i])+"\n")
f.close()
