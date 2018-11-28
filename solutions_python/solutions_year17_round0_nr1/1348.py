import sys

def flip( ch ):
    if ch =='-':    return '+'
    return '-'

for cases in xrange( int( sys.stdin.readline() ) ):
    out = "Case #%d: "%( cases + 1 )
    inp = sys.stdin.readline().strip().split()
    S, K = list(inp[0]), int( inp[1] )
    count = 0
    for i in xrange( len(S) - K + 1 ):
        if S[i] == '-':
            count += 1
            for j in xrange( i, i + K ):
                S[j] = flip( S[j] )
            #print S

    if S.count('-') > 0:    out += "IMPOSSIBLE"
    else:   out += str( count )
    print out

    
            
        
        
