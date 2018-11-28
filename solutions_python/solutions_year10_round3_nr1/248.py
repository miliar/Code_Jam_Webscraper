T = int(raw_input())

for t in range(1, T+1):
    intersectCount = 0
    N = int(raw_input())
    A_B = []
    for n in range(0,N):
        A_B.append(tuple(map(int, raw_input().split())))
    A_B.sort()
    
    current = []
    for A, B in A_B:
        current.append(B)
        current.sort()
        
        pos = 0
        for i, j in enumerate(current):
            if j == B:
                pos = i
                break
        
        intersectCount += len(current)-pos-1

    print 'Case #%d: %d' % (t, intersectCount)