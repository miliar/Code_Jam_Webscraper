import re

def getNstrPos(L, N):
    result = []
    def isConsonant(val):
        if val in ['a','e','i','o','u']:
            return 0
        else:
            return 1
    temp = map(isConsonant,L)
    #pring L,N,temp
    for i in xrange(len(L)):
        #pring (i + N), len(L), temp[i] == 1,sum(temp[i:i+N]) == N
        if (i + N) <= len(L) and temp[i] == 1 and sum(temp[i:i+N]) == N:
            result.append(i)
            
    return result

def processData(fileName):
    f = open(fileName)
    
    T = int(f.readline().strip())
    
    for i in xrange(1, T+1):
        L,N = [val for val in f.readline().strip().split(' ')]
        
        N = int(N)
        pos = getNstrPos(L,N)

        #pring pos
        ant = 0;
        substrings = 0
        first = True
        
        for val in pos:
            #pring val, ant, len(L), N
            preVal = val - ant
            postVal = len(L) - val - N
            
            substrings += preVal + 1 + (preVal + 1) * postVal
            #pring substrings
            if not first:
                substrings -= 1
                substrings -= postVal
            ant = val
            first = False

        print "Case #" + str(i) + ": " + str(substrings)



processData("A-small-attempt0.in")
