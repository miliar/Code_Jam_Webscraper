
def solve(N, C, M, P, B):
    count = [0] * 10001
    maxCount = 0
    for x in B:
        count[x] += 1
        if count[x] > maxCount:
            maxCount = count[x]

    emptySlot = []
    score = 0
    position = 1
    positionCount = 0
    for x in sorted(P):
        if x > position:
            for i in range(maxCount-positionCount):
                emptySlot.append(position)
            for i in range(position+1, x):
                for j in range(maxCount):
                    emptySlot.append(i)
            position = x
            positionCount = 0
        positionCount += 1
        if positionCount > maxCount:
            if len(emptySlot):
                t = emptySlot.pop()
                score += position - t
            else:
                maxCount += 1
                for i in range(1, position):
                    emptySlot.append(i)
                emptySlot.sort()

    emptySlot = []
    score = 0
    position = 1
    positionCount = 0


    for x in sorted(P):
        if x > position:
            for i in range(maxCount-positionCount):
                emptySlot.append(position)
            for i in range(position+1, x):
                for j in range(maxCount):
                    emptySlot.append(i)
            position = x
            positionCount = 0
        positionCount += 1
        if positionCount > maxCount:
            if len(emptySlot):
                t = emptySlot.pop()
                score += 1 #position - t
            else:
                maxCount += 1
                for i in range(1, position):
                    emptySlot.append(i)
                emptySlot.sort()

    return str(maxCount) + ' ' + str(score)


T = int(input())
for i in range(1, T+1):
    N, C, M  = [int(x) for x in input().split(' ')]
    P = []
    B = []
    for j in range(M):
        a, b = [int(x) for x in input().split(' ')]
        P.append(a)
        B.append(b)
    print('Case #{}: {}'.format(i, solve(N, C, M, P, B)))
