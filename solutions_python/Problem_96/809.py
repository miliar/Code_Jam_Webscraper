from itertools import permutations

def num( N, S, p, total ):
    max_cntr = 0    
    for scores in permutations( total ):
        # Non valid set
        if S > 0 and min( scores[:S] ) < 2:
            continue
        i    = 0
        cntr = 0
        while i < len(scores):
            base = scores[i] / 3
            left = scores[i] - base * 3
            
            if i < S:
                # Handling unusual results
                if left == 0:
                    best = base + 1
                elif left == 1:
                    best = base + 1
                elif left == 2:
                    best = base + 2
            else:
                # Handling usual results
                if left == 0:
                    best = base
                elif left == 1:
                    best = base + 1
                elif left == 2:
                    best = base + 1
            # print best
            if best >= p:
                cntr += 1
            i += 1
        if cntr > max_cntr:
            max_cntr = cntr
    return max_cntr

f = open( "input", "r")
cntr = int( f.readline() )

j = 1
for i in range(cntr):
    data = [ int(x) for x in f.readline().split(" ") ]
    N = data[0]
    S = data[1]
    p = data[2]
    print "Case #" + str(j) + ": " + str( num( N, S, p, data[3:] ) )
    j += 1
