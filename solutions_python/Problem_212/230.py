# I run this with python 3.4.3

import numpy as np # used for arrays e.g.; Can be downloaded from www.numpy.org

# I use filenames for input/output
debug=False
#filename = 'sample.in'
filename = 'A-small-attempt0.in'
outputFilename = filename.replace('in','out')

def runAlgorithm( N, P, groupSizes ):
    assert P in [2,3]
    if P == 2:
        modZeroCount = 0
        modOneCount = 0
        for g in groupSizes:
            if g % 2 == 0:
                modZeroCount += 1
            else:
                modOneCount += 1
        return modZeroCount + modOneCount//2 + modOneCount%2
    elif P == 3:
        modZeroCount = 0
        modOneCount = 0
        modTwoCount = 0
        for g in groupSizes:
            if g % 3 == 0:
                modZeroCount += 1
            elif g%3 == 1:
                modOneCount += 1
            else:
                modTwoCount += 1
        alternateOneTwoCount = min( modOneCount, modTwoCount )
        singleCount = max( modOneCount, modTwoCount ) - alternateOneTwoCount
        lastByte = 1 if singleCount%3 != 0 else 0
        return modZeroCount + alternateOneTwoCount + singleCount//3 + lastByte

# handle file input/output and call above algorithm for each case
open( outputFilename, 'w' ) # clear output file
with open(filename, 'r') as f:
    caseCount = int( f.readline().strip() )
    for i in range( 1, caseCount+1 ):
        print('i:', i) # show progress
        data = f.readline().strip().split(' ')
        N = int( data[0] )
        P = int( data[1] )
        data = f.readline().strip().split(' ')
        GroupSizes = [ int(d) for d in data ]
        result = runAlgorithm( N, P, GroupSizes )
        with open( outputFilename, 'a' ) as f2:
            outputLine = 'Case #{}: '.format(i) + '{}'.format(result)
            if debug:
                print(outputLine)
            f2.write( outputLine + '\n')
            
