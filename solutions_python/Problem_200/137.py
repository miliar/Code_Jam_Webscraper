# I run this with python 3.4.3

# I use filenames for input/output
debug=True
#filename = 'sample.in'
#filename = 'B-small-attempt0.in'
filename = 'B-large.in'
outputFilename = filename.replace('in','out')

def flip( seq ):
    out=[]
    for c in seq:
        if c == '+':
            out.append( '-' )
        elif c == '-':
            out.append( '+' )
        else:
            raise ValueError( c )
    return out

# This is the core of my program
def runAlgorithm( N ):
    if N < 10:
        return N
    NString = [v for v in str(N)]
    while True:
        for i in range(len(NString)-1):
            if NString[i] > NString[i+1]:
                break
            elif i == len(NString)-2:
                return int( "".join(NString) )
        NString[i] = chr( ord(NString[i])-1 )
        NString[i+1:] = ['9'] * (len(NString)-i-1)
    
        

# handle file input/output and call above algorithm for each case
open( outputFilename, 'w' ) # clear output file
with open(filename, 'r') as f:
    caseCount = int( f.readline().strip() )
    for i in range( 1, caseCount+1 ):
        print('i:', i) # show progress
        N = int( f.readline().strip() )
        if debug:
            print('N:', N)
        output = runAlgorithm( N ) # call algorithm for single case
        with open( outputFilename, 'a' ) as f2:
            outputLine = 'Case #{}: '.format(i) + str(output)
            if debug:
                print(outputLine)
            f2.write( outputLine + '\n')
            
