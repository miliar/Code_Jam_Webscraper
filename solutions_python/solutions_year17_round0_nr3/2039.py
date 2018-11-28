def calcStallVals(stlls):
    stallVals = []
    for i, s in enumerate(stlls):
        ls, rs = 0, 0
        il, ir = i - 1, i + 1
        while il >= 0:
            if stalls[il]:
                ls += 1
            else:
                break
            il -= 1
        while ir < N + 2:
            if stalls[ir]:
                rs += 1
            else:
                break
            ir += 1
        stallVals.append((ls, rs))
    return stallVals

t = int(input())

for case in range(t):
    N, K = [int(x) for x in input().split()]
    stalls = [False] + [True] * N +[False]

    a = ''

    for kK in range(K):
        stallVals = calcStallVals(stalls)

        maxMin = 0
        for i, sV in enumerate(stallVals):
            if stalls[i] and min(sV) > maxMin:
                maxMin = min(sV)

        maxMax = 0
        targetStalls = []
        for i, sV in enumerate(stallVals):
            if stalls[i] and min(sV) == maxMin:
                targetStalls.append(i)
                if max(sV) > maxMax:
                    maxMax = max(sV)

        if len(targetStalls) > 1:
            tempTargetVals = []
            for i in targetStalls:
                if max(stallVals[i]) == maxMax:
                    tempTargetVals.append(i)
            targetStalls = tempTargetVals

        stalls[targetStalls[0]] = False
        ls, rs = stallVals[targetStalls[0]-1]
        stallVals[targetStalls[0] - 1] = ls, 0
        ls, rs = stallVals[targetStalls[0] + 1]
        stallVals[targetStalls[0] + 1] = 0, rs

        if kK == K - 1:
            a = '{} {}'.format(maxMax, maxMin)

    print('Case #{}: {}'.format(case + 1, a))
