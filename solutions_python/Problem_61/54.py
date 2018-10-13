#

MAX_N = 25 # 25

answers = [0]*(MAX_N+1)

for i in xrange( 1<<(MAX_N-2) ):
    
    #array = []
    #
    #for j in xrange( MAX_N ):
    #    
    #    if i&(1<<j):
    #        
    #        array.append( j+2 )
    #
    #array.append( MAX_N )
    current = MAX_N
    
    while current != 1:
        
        if ((1<<(current-2)) & i) or current == MAX_N:
            
            index = 1
            for j in xrange( 0, current-2 ):
                
                if (1<<j)&i: index += 1
            
            current = index
        
        else: break
    else:
        
        for n in xrange( MAX_N, 2, -1 ):
            
            answers[n] += 1
            
            if (i&(1<<(n-3))):
                
                break

answers[2] = 1

T = int( raw_input() )

for t in xrange( 1, T+1 ):
    
    n = int( raw_input() )
    print "Case #%d: %d" % (t, answers[n]%100003)
