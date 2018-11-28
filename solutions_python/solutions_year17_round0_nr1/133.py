# I use filenames for input/output
debug=False
#filename = "sample.in"
#filename = "A-small-attempt0.in"
filename = "A-large.in"
outputFilename = filename.replace("in","out")

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
def runAlgorithm( S, K ):
    flipCount = 0
    while True:
        try:
            index = S.index('-')
        except ValueError:
            return flipCount
        if index > len(S) - K:
            return "IMPOSSIBLE"
        else:
            S[index:index+K] = flip( S[index:index+K] )
            flipCount += 1
        #print( flipCount, ''.join(S) )
        

# handle file input/output and call above algorithm for each case
open( outputFilename, "w" ) # clear output file
with open(filename, "r") as f:
    caseCount = int( f.readline().strip() )
    for i in range( 1, caseCount+1 ):
        print("i:", i) # show progress
        data = f.readline().strip().split(' ')
        S = [ v for v in data[0] ]
        K = int( data[1] )
        if debug:
            print("S:", ''.join(S))
            print("K:", K)
        output = runAlgorithm( S, K ) # call algorithm for single case
        with open( outputFilename, "a" ) as f2:
            outputLine = "Case #{}: ".format(i) + str(output)
            if debug:
                print(outputLine)
            f2.write( outputLine + "\n")
            
