# Problem CodeJam 2010 1B - B
# Author John Schroder
    
    
def run( N, K, B, T, X, V ):  
    inBarn = set() 
    maxSwaps = 0
    totalSwaps = 0
    if len(inBarn) >= K:
        return totalSwaps
    for c in range(1, N+1):
        maxDistance = X[c-1] + T*V[c-1]
        if B > maxDistance :  # can't make barn too slow
            #print "Chicken %d too slow %d > %d " % (c, B, maxDistance)
            maxSwaps = maxSwaps+1
            #print "maxSwaps now ", maxSwaps
            continue 

        #print "Chicken %d goes in with %d swaps"% (c, maxSwaps)
        totalSwaps = totalSwaps + maxSwaps
        inBarn.add(c)
        if len(inBarn) >= K:
            return totalSwaps 
    
    return "IMPOSSIBLE"
     


inputFile = "B-large.in"
outputFile = "B-large.out"
output = open(outputFile,"w")
input = open(inputFile,"r")

line = input.readline().strip()
nCases = int(line)
for nCase in range(1, nCases+1):
    tokens = input.readline().strip().split()
    N = int(tokens[0])
    K = int(tokens[1])
    B = int(tokens[2])
    T = int(tokens[3])

    X = [ int(t) for t in input.readline().strip().split() ]
    V = [ int(t) for t in input.readline().strip().split() ]
    
    X.reverse()
    V.reverse() 
    
    print >> output,"Case #%d: %s" % ( nCase, run( N, K, B, T, X, V ) )
    
    