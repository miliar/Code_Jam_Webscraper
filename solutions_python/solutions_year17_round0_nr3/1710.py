tc_num = int(input())
N, K, j = 0, 0, 0
stall = []

def even(num):
    return num % 2 == 0

def getLR(dist):
    if dist == 0: return 0, 0
    l, r = dist // 2, dist // 2
    if even(dist):
        l -= 1
    return l, r

def minStall(s):
    l, r = getLR(s)
    return min(l, r)

def maxStall(s):
    l, r = getLR(s)
    return max(l, r)

def divStall():
    global stall
    if len(stall) > 0:
        #  stall.sort(key = int, reverse = True)
        minListIndex = []
        mostMinValue = 0
        mostMinCount = 0
        mostMinIndex = 0
        for i, s in enumerate(stall):
            if minStall(s) > mostMinValue:
                mostMinCount = 1
                mostMinValue = minStall(s)
                mostMinIndex = i
                minListIndex.clear()
                minListIndex.append(i)
            elif minStall(s) == mostMinValue:
                mostMinCount += 1
                minListIndex.append(i)
            elif minStall(s) < mostMinValue:
                break
        # Check if only one such stall
        if mostMinCount == 1:
            mostMin = stall[mostMinIndex]
            del stall[mostMinIndex]
            l, r = getLR(mostMin)
            if l > 0: stall.append(l)
            if r > 0: stall.append(r)
            return mostMin
        else: # Check for max
            mostMaxValue = 0
            mostMaxCount = 0
            mostMaxIndex = 0
            for i in minListIndex:
                if maxStall(stall[i]) > mostMaxValue:
                    mostMaxCount = 1
                    mostMaxValue = maxStall(stall[i])
                    mostMaxIndex = i
                elif maxStall(stall[i]) == mostMaxValue:
                    mostMaxCount += 1
            mostMax = stall[mostMaxIndex]
            del stall[mostMaxIndex]
            l, r = getLR(mostMax)
            if l > 0: stall.append(l)
            if r > 0: stall.append(r)
            return mostMax
    else:
        l, r = N // 2, N // 2
        if even(N):
            l -= 1
        if l > 0: stall.append(l)
        if r > 0: stall.append(r)
        return N

def batchAssign():
    global K
    global stall
    global j
    if len(stall) == 0:
        divStall()
        K -= 1
        return

    maxVal = 0
    maxList = 0
    stall.sort(key = int, reverse = True)
    #  stall.sort()
    for s in stall:
        if s >= maxVal:
            maxVal = s
            maxList += 1
        else:
            break

    if K > maxList:
        del stall[:maxList]
        for i in range(0, maxList):
            l, r = getLR(maxVal)
            if l > 0: stall.append(l)
            if r > 0: stall.append(r)
        K -= maxList
        return
        #  print(stall)
    else:
        del stall[:K-1]
        for i in range(0, K-1):
            l, r = getLR(maxVal)
            if l > 0: stall.append(l)
            if r > 0: stall.append(r)
        K = 1
        return

def getLast():
    if len(stall) == 0:
        return N
    stall.sort(key = int, reverse = True)
    return stall[0]

for i in range(0, tc_num):
    N, K = map(int, input().split())
    stall = []
    j = 0

    if N != K:
        while K > 1:
            batchAssign()

        s = getLast()
        minVal = minStall(s)
        maxVal = maxStall(s)

        print("Case #{}: {} {}".format(i + 1, maxVal, minVal))
    else:
        print("Case #{}: 0 0".format(i + 1))
