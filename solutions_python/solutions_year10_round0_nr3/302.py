#Author John Schroder

import sys
#Author John Schroder

def processGroup( head, k, N, groups):
    gSize = 0
    startingHead = head
    while True:
        g = groups[ head ]
        if gSize + g > k:
            return head, gSize
        gSize = gSize + g
        head = (head + 1 ) % N
        if head == startingHead:
            return head, gSize

def calcGroup( nCase, R, k, N, groups, out ): 
    head = 0
    totalSales = 0
    for _i in range(R):
        head, gSize = processGroup( head, k, N, groups)
        totalSales = totalSales + gSize
    out.write( "Case #%d: %d\n" % (nCase, totalSales))
    
    
def process( inFilename, outFilename ):
    f = open(inFilename, 'r')
    out = open( outFilename, "w" )
    line = f.readline().strip() 
    
    nCases = int(line)
    for nCase in range(1, nCases+1):
        tokens = f.readline().strip().split()
        R = int( tokens[0] )
        k = int( tokens[1] )
        N = int( tokens[2] )
        tokens = f.readline().strip().split()
        groups = [ int( t ) for t in tokens ]
        calcGroup( nCase, R, k, N, groups, out )
    
if __name__ == "__main__": 
    process( sys.argv[1], sys.argv[2] )  
