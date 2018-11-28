import numpy as np

with open('in.txt') as f:
    lines = f.readlines()

numCases = int(lines[0])
for caseNum in xrange(1, numCases+1):
    numShrooms = np.array(map(int, lines[caseNum*2].split()))
    changes = numShrooms[1:] - numShrooms[:-1]

    # total negative change
    y = sum([ -change for change in changes if change<0 ])

    # maximum negative change
    eatingRate = - changes.min()
    if eatingRate < 0:
        eatingRate = 0
    # print '   ', eatingRate

    # before each point add extra mushrooms so it matches unless we are supposed to be zero
    current = numShrooms[0]
    totalEaten = 0
    for i in xrange(1, len(numShrooms)):

        # eat out rate or we hit zero
        afterEat = current - eatingRate
        if afterEat < 0:
            afterEat = 0

        numEaten = current - afterEat
        # print '  numEaten: ', numEaten
        assert numEaten >= 0
        totalEaten += numEaten
        current -= numEaten

        assert current <= numShrooms[i]
        current = numShrooms[i]   # pile on

        # eaten = max(current + eatingRate, 0)
        # current += eatingRate  # note eatingRate == 0
        # if current < 0:
        #     current = 0
        # # print current, numShrooms[i]
        # assert current <= numShrooms[i]
        # if current < numShrooms[i]:
        #     assert numShrooms[i] >= 0
        #     if numShrooms[i] == 0:
        #         current = 0
        #     else:
        #         added = numShrooms[i] - current
        #         current += added
        #         totalAdded += added
        #         print 'added: ', added



    print 'Case #{}: {} {}'.format(caseNum, y, totalEaten)
