import os
import sys

n = int( sys.stdin.readline().strip() )

for i in range( n ):
    R, k, N = sys.stdin.readline().strip().split(' ')
    R = int(R)
    k = int(k)
    N = int(N)

    groups = [ int(x) for x in sys.stdin.readline().strip().split(' ') ]
    queue = [ x for x in groups ]
    qbeg = 0
    tot = 0
    cache = {}
    cache_nextbeg = {}
    begs = []
    begs_costs = []
    beg_rep = -1
    while 1:
        if qbeg in begs:
            beg_rep = qbeg
            beg_rep_i = begs.index( qbeg )
            break
        begs.append( qbeg )
        
        currk = k
        toqueue = []
        
        while len( queue ) > 0 and queue[0] <= currk:
            toqueue.append( queue[0] )
            currk -= queue[0]
            del queue[0]
        
        begs_costs.append( k - currk )

        qbeg = ( qbeg + N - len( queue ) ) % N
        
        # ride
        tot += k - currk
        queue += toqueue
    # adjust
    #if len( begs ) > 1 and ( begs[ -1 ] < begs[ -2 ] ) and( begs[-1] - begs[0] != begs[-2] - begs[-1] ):
    #    first_round = [ x for x in begs if x < begs[-1] ]
    #    first_round_costs = begs_costs[:len(first_round)]

    #    begs = begs[len(first_round):]
    #    begs_costs = begs_costs[len(first_round):]
    #else:
    #    first_round = []
    #    first_round_costs = []
    
    first_round = begs[ : beg_rep_i ]
    first_round_costs = begs_costs[ : beg_rep_i ]
    begs = begs[ beg_rep_i : ]
    begs_costs = begs_costs[ beg_rep_i : ]
    
    frc = sum( first_round_costs )

    wholeround = (R-len(first_round)) / len( begs )
    rest = (R-len(first_round)) % len(begs)

    wholeround_cost = sum(begs_costs)
    res_cost = sum( begs_costs[:rest] )

    tot = frc +  wholeround_cost * wholeround + res_cost


            
        
    print 'Case #%d: %d' % ( i+1, tot, )


