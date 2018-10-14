# I run this with python 3.4.3

# I use filenames for input/output
debug=True
#filename = 'sample.in'
#filename = 'C-small-2-attempt0.in'
filename = 'C-large.in'
outputFilename = filename.replace('in','out')

# This is the core of my program
def runAlgorithm( N, K ):
    intervals = {N:1}   # dict is not most efficient here, but seems to be sufficient
    KReached=0
    while True:
        #print(intervals)
        maxInterval = max(intervals.keys())
        count = intervals.pop( maxInterval )
        if KReached + count >= K:
            #print(intervals)
            vals = [(maxInterval-1) // 2, (maxInterval-1) - (maxInterval-1) // 2]
            return "{} {}".format( max(vals), min(vals) )
        for newInterval in [ (maxInterval-1) // 2, (maxInterval-1) - (maxInterval-1) // 2]:
            if newInterval in intervals:
                intervals[newInterval] += count
            else:
                intervals[newInterval] = count
        KReached += count
    
        

# handle file input/output and call above algorithm for each case
open( outputFilename, 'w' ) # clear output file
with open(filename, 'r') as f:
    caseCount = int( f.readline().strip() )
    for i in range( 1, caseCount+1 ):
        print('i:', i) # show progress
        data = f.readline().strip().split(' ')
        N = int( data[0] )
        K = int( data[1] )
        if debug:
            print('N:', N)
            print('K:', K)
        output = runAlgorithm( N, K ) # call algorithm for single case
        with open( outputFilename, 'a' ) as f2:
            outputLine = 'Case #{}: '.format(i) + str(output)
            if debug:
                print(outputLine)
            f2.write( outputLine + '\n')
            
