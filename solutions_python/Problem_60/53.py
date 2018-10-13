#

C = int( raw_input() )

for c in xrange( 1, C+1 ):
    
    N, K, B, T = map( int, raw_input().split() )
    
    positions = map( int, raw_input().split() )
    velocities = map( int, raw_input().split() )
    
    swaps = 0
    
    for k in xrange( K ):
        
        for i in xrange( N-1-k, -1, -1 ):
            
            timeTaken = (B-positions[i]+velocities[i]-1)/velocities[i]
            
            if timeTaken > T:
                
                swaps += 1
            
            else:
                
                del positions[i]
                del velocities[i]
                break
        
        else:
            
            swaps = -1
            break
    
    if swaps == -1:
        
        print "Case #%d: IMPOSSIBLE" % (c)
    
    else:
        
        print "Case #%d: %d" % (c, swaps)
