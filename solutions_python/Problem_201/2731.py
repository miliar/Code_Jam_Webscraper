def findSpacing(n, stalls):
    for i in range(n):
        options = []
        maxGap = 0
        start = 0
        gapFlag = 0
        for j in range(len(stalls)):
            if gapFlag == 0 and stalls[j] == 0:
                start = j
                gapFlag = 1
            if gapFlag == 1 and stalls[j] == 1:
                gapFlag = 0
                if (j-1) - start > maxGap:
                    maxGap = (j-1) - start
                    options = [(start,j-1)]
                elif (j-1) - start == maxGap:
                    options.append((start,j-1))
        gap = options[0]
        gapWidth = (gap[1] - gap[0]) // 2
        place = gap[0] + gapWidth
        stalls[place] = 1
    return max(place-gap[0], gap[1]-place), min(place-gap[0], gap[1]-place)


t = int(input())

for i in range(t):
    n,k = map(int, input().split())
    stalls = [1] + ([0] * (n)) + [1]
    y, z = findSpacing(k, stalls)
    print("Case #" + str(i+1) + ": " + str(y) + " " + str(z))
