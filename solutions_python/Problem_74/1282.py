import sys
from collections import deque

#returns ([(counter,buttonIndex)],[(counter,buttonIndex)])

def compute(data):
    global nButtons
    blue = deque(data[0])
    orange = deque(data[1])
    time = 0
    bPos = 1
    oPos = 1
    bTgt = blue.popleft() if len(blue) > 0 else (9000,1)
    oTgt = orange.popleft() if len(orange) > 0 else (9000,1)
    current = 1
    blueWay = False
    #print "orangetgt=" + str(oTgt[1])
    
    while current <= nButtons:
        #print current
        
        blueWay = bTgt[0] < oTgt[0]
        blueOnBt = bTgt[1] == bPos
        orangeOnBt = oTgt[1] == oPos

        #print blueWay
        #print "orange: " + str(oPos)
        
        if(blueWay):
            if(blueOnBt):
                #blue press
                current = current + 1
                if (len(blue) > 0):
                    bTgt = blue.popleft()
                else:
                    bTgt = (9000,1)
            else:
                bPos = move(blueOnBt,bPos,bTgt[1])
            oPos = move(orangeOnBt,oPos,oTgt[1])
        else:
            if(orangeOnBt):
                #orange press
                current = current + 1
                if (len(orange) > 0):
                    oTgt = orange.popleft()
                else:
                    oTgt = (9000,1)
            else:
                oPos = move(orangeOnBt,oPos,oTgt[1])
            bPos = move(blueOnBt,bPos,bTgt[1])

        time = time + 1

    return time

def move(cond, pos,tgt):
    if(cond):
        return pos
    else:
        if(pos < tgt):
            return pos+1
        else:
            return pos-1


def parseData(line):
    global nButtons
    tokens = line.split()
    nButtons = int(tokens[0])
    #print "nButtons: " + str(nButtons)
    blueList = []
    orangeList = []

    i = 1
    counter = 1
    while i < len(tokens):
        tok = tokens[i]
        btInd = int(tokens[i+1])
        if(tok == "O"):
            blueList.append((counter,btInd))
        else:
            orangeList.append((counter,btInd))

        counter = counter + 1
        i = i + 2
                              
    return (blueList,orangeList)
                              
nTests = int(sys.stdin.readline())
nButtons = 0

for i in range(nTests):
    data = parseData(sys.stdin.readline())
    #print str(data)
    time = compute(data)
    print "Case #" + str(i+1) + ": " + str(time)
