import sys

with open( sys.argv[1] ) as dataFile:
    currentCase = 1
    numCases = dataFile.readline()
    for unsplitLine in dataFile:
        count = 0
        splitLine = unsplitLine.split()
        numGooglers = int( splitLine[0] )
        surprisingScores = int( splitLine[1] )
        bestResult = int( splitLine[2] )
        validScores = [ int( score ) for score in splitLine[3:] if int( score ) >= ( 3 * bestResult - 4 ) and int( score ) >= bestResult ]
        validScores.sort()
        if len( validScores ) > 0:
            for i in range( 0, surprisingScores ):
                if len( validScores ) > 0:
                    validScores.pop( 0 )
                    count += 1
            validScores = [ score for score in validScores if score >= 3 * bestResult - 2 ]
            count += len( validScores )
        print "Case #%s: %s" % ( currentCase, count )
        currentCase += 1

