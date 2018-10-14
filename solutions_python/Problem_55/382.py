import os
import sys
import string 


T = int( sys.stdin.readline() ); 

for t in range( 0, T ): 
    ln0 = sys.stdin.readline() 
    ln1 = sys.stdin.readline() 

    #print '---------------------------------'
    #sys.stdout.write( ln0 )
    #sys.stdout.write( ln1 )

    w = string.split( ln0 )
    R = int( w[0] )
    k = int( w[1] )
    N = int( w[2] )

    groups = [ 0 ] * N
    packed = [ 0 ] * N 
    nextidx = [ 0 ] * N

    w = string.split( ln1 ) 
    cursor = 0
    for ww in w: 
       groups[ cursor ] = int( ww ); 
       cursor = cursor + 1 
    
    cursor = 0; 
    totalPeople = 0; 
    remainingRuns = R
    while remainingRuns > 0:  
        if packed[ cursor ] == 0:
            oldcursor = cursor
            ridecount = 0
            remaininggroups = N
            while ridecount <= k and remaininggroups >= 0: 
                ridecount = ridecount + groups[ cursor ]
                lastcursor = cursor
                cursor = ( cursor + 1 ) % N  
                remaininggroups = remaininggroups - 1
            ridecount = ridecount - groups[ lastcursor] 
            cursor = lastcursor 

            packed[ oldcursor ] = ridecount;
            nextidx[ oldcursor ] = cursor; 
            
            totalPeople = totalPeople + ridecount 
            remainingRuns = remainingRuns - 1; 

            #print 'roundpeople' , ridecount, ' total people ' , totalPeople, ' rr ' , remainingRuns 
        else:
            #Detect the cicle 
            ii = cursor
            partialSum = packed[cursor]
            partialLen = 1
            while( nextidx[ ii ] != cursor ):
                ii = nextidx[ ii ] 
                partialLen = partialLen + 1
                partialSum = partialSum + packed[ii]
            #
            #print 'partialSum' , partialSum, partialSum
            mult = remainingRuns / partialLen
            totalPeople = totalPeople + mult * partialSum
            remainingRuns = remainingRuns % partialLen; 

            #print ' mult ' , mult, ' totalPeople ', totalPeople , ' rr ' , remainingRuns  
            
            while remainingRuns > 0: 
                #print ' packed ' , packed[ cursor ], ' cur ' , cursor 
                totalPeople = totalPeople + packed[ cursor ] 
                cursor = nextidx[ cursor ]
                remainingRuns = remainingRuns - 1
    
    sys.stdout.write( 'Case #' );
    sys.stdout.write( str( t + 1 ) );
    sys.stdout.write( ': ' ); 
    print totalPeople
