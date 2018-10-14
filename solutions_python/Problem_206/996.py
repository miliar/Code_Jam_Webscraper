# I run this with python 3.6.1

# I use filenames for input/output
debug=False
#filename = 'sample.in'
#filename = 'A-small-attempt0.in'
filename = 'A-large.in'
outputFilename = filename.replace('in','out')

def runAlgorithm( D, N, K, S ):
    timeNeeded = 0
    for i in range(N):
        thisTime = (D-K[i]) / S[i]
        timeNeeded = max( timeNeeded, thisTime )
    return D / timeNeeded

# handle file input/output and call above algorithm for each case
open( outputFilename, 'w' ) # clear output file
with open(filename, 'r') as f:
    caseCount = int( f.readline().strip() )
    for i in range( 1, caseCount+1 ):
        print('i:', i) # show progress
        data = f.readline().strip().split(' ')
        D = int( data[0] ) # distance
        N = int( data[1] ) # # other horses
        if debug:
            print('N:', N)
            print('M:', M)
        K = [] # init. pos.
        S = [] # max. speed
        for h in range(N):
            data = f.readline().strip().split(' ')
            K.append( int( data[0] ) )
            S.append( int( data[1] ) )
        result = runAlgorithm( D, N, K, S )
        with open( outputFilename, 'a' ) as f2:
            outputLine = 'Case #{}: '.format(i) + '{:.6f}'.format(result)
            if debug:
                print(outputLine)
            f2.write( outputLine + '\n')
            
