def ratat(N, R, P, Q):
    indexes = [0]*N

    normQ = [[float(Q[i][j])/float(R[i]) for j in xrange(P)] for i in xrange(N)]

    for i in xrange(N):
         normQ[i].sort()

    current = [normQ[i][0] for i in xrange(N)]
    
    inRange = True

    numKits = 0

    while inRange:
        current = [normQ[i][indexes[i]] for i in xrange(N)]
        if makesRecipe(current):
            numKits += 1
            for i in xrange(N):
                indexes[i] += 1
                if indexes[i] >= P:
                    inRange = False
        else:
            lowest = minIndex(current)
            indexes[lowest] += 1
            if indexes[lowest] < P:
                current[lowest] = normQ[lowest][indexes[lowest]]
            else:
                inRange = False

    return numKits

def makesRecipe(ingredients):
    upperBound = min(ingredients) / 0.9
    lowerBound = max(ingredients) / 1.1

    if lowerBound <= upperBound and lowerBound <= int(upperBound):
        return True
    else:
        return False

def minIndex(A):
    current = A[0]
    currentIndex = 0
    for i in xrange(len(A)):
        if A[i] < current:
            current = A[i]
            currentIndex = i
    return currentIndex

t = int(raw_input())

for x in xrange(1, t+1):
    N, P = raw_input().split(' ')
    N = int(N)
    P = int(P)
    R = raw_input().split(' ')
    Q = []
    for i in xrange(N):
        Q.append(raw_input().split(' '))
    print 'Case #{}: {}'.format(x, ratat(N,R,P,Q))
       
            
    