#

T = int( raw_input() )

for t in xrange( 1, T+1 ):
    
    N, M = map( int, raw_input().split() )
    dirs = set()
    
    for i in xrange( N ):
        
        dirs.add( raw_input() )
    
    ans = 0
    
    for i in xrange( M ):
        
        path = raw_input().split( "/" )[1:]
        
        current = ""
        
        for p in path:
            
            current += "/" + p
            if current not in dirs:
                
                ans += 1
                dirs.add( current )
    
    print "Case #%d: %d" % (t, ans)