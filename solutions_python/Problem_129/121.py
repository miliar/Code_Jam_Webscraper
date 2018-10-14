import sys

caseCount = int(sys.stdin.readline().split()[0])
for caseIndex in range(caseCount):
    stopCount, pairCount = map(int, sys.stdin.readline().split())
    stopPeople = [0] * (stopCount + 1)
    loss = 0
    for i in range(pairCount):
        start, end, people = map(int, sys.stdin.readline().split())
        if start != end:
            loss = loss + ((2 * stopCount - (end - start - 1)) * (end - start) / 2) * people
            for j in range(start, end):
                stopPeople[j] = stopPeople[j] + people
    for i in range(1, stopCount):
        while stopPeople[i]:
            j = i
            while stopPeople[j + 1]:
                j = j + 1
            loss = loss - (2 * stopCount - (j - i)) * (j - i + 1) / 2
            for k in range(i, j + 1):
                stopPeople[k] = stopPeople[k] - 1
    print('Case #%d: %d' % (caseIndex + 1, loss % 1000002013))
    
