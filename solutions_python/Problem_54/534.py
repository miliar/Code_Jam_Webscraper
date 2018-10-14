#Author John Schroder

import sys


def calcGcd( a, b ): 
    if a < b:
        tmp = a
        a = b
        b = tmp
        
    remainder = a % b
    while remainder != 0:
        a = b
        b = remainder
        remainder = a % b
    return b
         
def gcdList( data ):
    while True:
        data = list(set(data))  
        data.sort() 
        if len(data) == 1:
            return data[0];
        gcds = set()
        minItem = data[0]
        for item in data[1:]:  
            gcds.add( calcGcd(minItem, item))
        data = list(gcds)
        
        
          
def calcFairWarning( nCase, N, times, out ): 
    diffs = []
    times.sort() 
    minTime = times[0]
    for i in range( 1, len( times) ): 
        if ( times[i] != minTime):
            diffs.append( times[i] - minTime )
    gcd = gcdList(diffs)
    apocalypse = - ( minTime % gcd )
    if apocalypse < 0 :
        apocalypse = apocalypse + gcd
    out.write( "Case #%d: %d\n" % (nCase, apocalypse))


def process( inFilename, outFilename ):
    f = open(inFilename, 'r')
    out = open( outFilename, "w" )
    line = f.readline().strip() 
    
    nCases = int(line)
    for nCase in range(1, nCases+1):
        tokens = f.readline().strip().split()
        N = int( tokens[0] )
        times = [ int( t ) for t in tokens[1:] ]
        times.sort()
        calcFairWarning( nCase, N, times, out )
    
    
if __name__ == "__main__": 
    process( sys.argv[1], sys.argv[2] )  
