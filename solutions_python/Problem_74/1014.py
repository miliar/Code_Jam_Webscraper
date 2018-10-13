#!/usr/bin/env python

inputFile = open( 'A-large.in' )
outputFile = open( 'A-large.out', 'w' )


# testcases
t = int(inputFile.readline())
c = 1

while c <= t: # MAIN LOOP
    line = inputFile.readline()
    
    orangeQ = []
    blueQ = []
    fullQ = []
    
    n = int(line[0])
    tempNum = ""
    tempColor = ""
    
    line = line.replace( ' ', '' )
    for i in line: # add each element to its queue
        if (i == 'O' or i == 'B'):
            if tempColor is not "":
                if tempColor == 'O':
                    orangeQ.append(int(tempNum))
                else:
                    blueQ.append(int(tempNum))
                
                fullQ.append(tempColor)
                
            tempNum = ""
            tempColor = i
        else:        
            tempNum += i
    
    if tempColor is not "":
        if tempColor == 'O':
            orangeQ.append(int(tempNum))
        else:
            blueQ.append(int(tempNum))
                
        fullQ.append(tempColor)
    
    secs = 0
    orange = 1
    blue = 1
    
    for e in fullQ:
        secsAv = 0 #seconds available
        if e == 'O':
            secsAv = abs(orangeQ[0] - orange) + 1 # seconds that the movement will take
            
            secs += secsAv # add those seconds to the total
            orange = orangeQ[0] # set orange to the new position
            orangeQ.remove(orangeQ[0]) # remove the position from the orange queue
            
            if blueQ:
                dif = blue - blueQ[0] # difference between blue actual and future position
                if abs(dif) > secsAv:
                    if dif > 0:
                        blue -= secsAv
                    else:
                        blue += secsAv
                else:
                    blue = blueQ[0]
        
        else:
            secsAv = abs(blueQ[0] - blue) + 1 # seconds that the movement will take
            secs += secsAv # add those seconds to the total
            blue = blueQ[0] # set orange to the new position
            blueQ.remove(blueQ[0]) # remove the position from the orange queue
            
            if (orangeQ):
                dif = orange - orangeQ[0] # difference between blue actual and future position
                if abs(dif) > secsAv:
                    if dif > 0:
                        orange -= secsAv
                    else:
                        orange += secsAv
                else:
                    orange = orangeQ[0]
    outputFile.write( "Case #" + str(c) + ": " + str(secs) + "\n")
    c += 1

outputFile.close()
inputFile.close()