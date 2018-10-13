__author__ = 'Glen'
numCases = int(input().strip())
for caseNum in range(numCases):
    C, F, X = map(float, input().strip().split())
    minTimeToX = None
    amount = 0
    rate = 2
    time = 0
    while True:
        timeToX = X / rate + time
        if minTimeToX is None or timeToX < minTimeToX:
            minTimeToX = timeToX
        else:
            break
        # Try buying another factory
        time += C / rate
        rate += F
    print('Case #{}: {}'.format(caseNum + 1, minTimeToX))