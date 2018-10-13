#Google code jam
#Qualifiers

inputList = []
outputNums = []

def parseInput( filename ):
    fd = open( filename )
    for line in fd:
        line = line.strip('\n')
        numberRange = line.split(' ')
        inputList.append( numberRange )
        outputNums.append(0)

    inputList.pop(0)
    outputNums.pop(0)

    fd.close()

def findOutputNums( inputNums ):
    for line in range( 0, len(inputNums) ):
        n = int(inputNums[line][0])
        m = int(inputNums[line][1])
        alreadyFoundPairs = []

        for i in range( n, m + 1 ):
            iStr = str(i)
            for count in range( 1, len(iStr) ):
                tempStr = iStr[count:len(iStr)] + iStr[0:count]
                #print( tempStr )
                tempInt = int(tempStr)

                tempPair = [i, tempInt]
                tempPairRev = [tempInt, i]
                if( tempInt >= n
                    and tempInt <= m
                    and len(iStr) == len(tempStr)
                    and tempInt > i
                    and tempPairRev not in alreadyFoundPairs                     
                    and tempPair not in alreadyFoundPairs ):
                    outputNums[line] += 1
                    alreadyFoundPairs.append( tempPair )
                    alreadyFoundPairs.append( tempPairRev )                    
                    #print( tempInt )

def outputCounts( countList ):

    fd = open("recyclednumbersoutput.txt", "w" )
    for i in range(0, len(countList) ):
        outputLine = "Case #" + str(i+1) + ": "
        outputLine += str(countList[i])
        fd.write( outputLine+"\n" )
                
                
        

parseInput( "test.txt" )
findOutputNums( inputList )
outputCounts( outputNums )

#print( inputList )
#print( outputNums )                    
