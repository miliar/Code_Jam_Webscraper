import math

testNum = int(input())

for i in range(1, testNum + 1):
    segments = {}
    capacity = 1
    segnow = 0
    maxd = 0
    mind = 0
    N, K = input().split(' ')
    N = int(N)
    K = int(K)
    if (N == K):
        maxd = mind = 0
        K = 0
    segnow = N
    while (K):
        if (capacity):
            maxd = math.ceil((segnow - 1) / 2)
            mind = math.floor((segnow - 1) / 2)
            if(segments.get(maxd)):
                segments[maxd] += 1
            else:
                segments[maxd] = 1
            if(segments.get(mind)):
                segments[mind] += 1
            else:
                segments[mind] = 1
            K -= 1
            capacity -= 1
        else:
            segnow = max(segments.keys())
            capacity = segments[segnow]
            segments.pop(segnow)

    print("Case #" + str(i) + ": " + str(maxd) + " " + str(mind))
